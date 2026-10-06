import pytest
import json
from app import app, questions_db


@pytest.fixture
def client():
    """Create a Flask test client for the application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    """Test GET /health returns 200 and status OK."""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == {"status": "OK"}


def test_get_syllabus_endpoint(client):
    """Test GET /api/syllabus returns the complete 7-subject structure."""
    response = client.get('/api/syllabus')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["semester"] == "Semester V"
    assert "subjects" in data
    assert len(data["subjects"]) == 7
    # Verify all subject codes
    codes = [s["subject_code"] for s in data["subjects"]]
    assert "2015111" in codes
    assert "2015112" in codes
    assert "2015113" in codes
    assert "2015114" in codes
    assert "2015115" in codes
    assert "2015116" in codes
    assert "2015511" in codes


def test_get_items(client):
    """Test GET /items retrieves questions list."""
    response = client.get('/items')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) >= 1
    # Check structure of the first question
    first_item = data[0]
    assert "id" in first_item
    assert "question" in first_item
    assert "option_a" in first_item
    assert "option_b" in first_item
    assert "option_c" in first_item
    assert "option_d" in first_item
    assert "answer" in first_item
    assert "subject" in first_item
    assert "subject_code" in first_item
    assert "module" in first_item
    assert "topic" in first_item
    assert "explanation" in first_item


def test_filtering_by_subject(client):
    """Test GET /items?subject=Computer Network and GET /items?subject_code=2015116."""
    res_sub = client.get('/items?subject=Computer%20Network')
    assert res_sub.status_code == 200
    data_sub = json.loads(res_sub.data)
    assert len(data_sub) > 0
    assert all(q["subject"] == "Computer Network" for q in data_sub)

    res_code = client.get('/items?subject_code=2015116')
    assert res_code.status_code == 200
    data_code = json.loads(res_code.data)
    assert len(data_code) == len(data_sub)
    assert all(q["subject_code"] == "2015116" for q in data_code)


def test_filtering_by_module_and_topic(client):
    """Test GET /items?module=3 and GET /items?topic=Subnetting."""
    res_mod = client.get('/items?subject_code=2015116&module=3')
    assert res_mod.status_code == 200
    data_mod = json.loads(res_mod.data)
    assert len(data_mod) > 0
    assert all(q["module_number"] == 3 for q in data_mod)

    res_topic = client.get('/items?topic=Subnetting')
    assert res_topic.status_code == 200
    data_topic = json.loads(res_topic.data)
    assert len(data_topic) >= 1
    assert any("subnetting" in q["topic"].lower() for q in data_topic)


def test_filtering_by_difficulty_and_type(client):
    """Test GET /items?difficulty=medium and GET /items?question_type=numerical."""
    res_diff = client.get('/items?difficulty=medium')
    assert res_diff.status_code == 200
    data_diff = json.loads(res_diff.data)
    assert len(data_diff) > 0
    assert all(q["difficulty"].lower() == "medium" for q in data_diff)

    res_type = client.get('/items?question_type=numerical')
    assert res_type.status_code == 200
    data_type = json.loads(res_type.data)
    assert len(data_type) > 0
    assert all(q["question_type"].lower() == "numerical" for q in data_type)


def test_post_item_success(client):
    """Test POST /items adds a new question with syllabus metadata."""
    new_question = {
        "question": "What is Docker Compose used for?",
        "option_a": "Defining and running multi-container Docker applications",
        "option_b": "Replacing the Linux operating system kernel",
        "option_c": "Hosting DNS server registries",
        "option_d": "Compiling Java bytecode to machine code",
        "answer": "A",
        "subject": "Agile Software Development and DevOps",
        "subject_code": "2015113",
        "module": "Module III - CI/CD Automation using Jenkins & Containerization using Docker",
        "module_number": 3,
        "topic": "Docker Compose",
        "explanation": "Docker Compose allows defining multi-container configurations in YAML.",
        "difficulty": "Easy",
        "question_type": "conceptual"
    }
    response = client.post(
        '/items',
        data=json.dumps(new_question),
        content_type='application/json'
    )
    assert response.status_code == 201
    created_data = json.loads(response.data)
    assert "id" in created_data
    assert created_data["question"] == new_question["question"]
    assert created_data["answer"] == "A"
    assert created_data["subject"] == "Agile Software Development and DevOps"
    assert created_data["subject_code"] == "2015113"
    assert created_data["module_number"] == 3
    assert created_data["topic"] == "Docker Compose"

    # Verify that GET /items now includes the new question
    get_res = client.get('/items')
    items = json.loads(get_res.data)
    assert any(item["id"] == created_data["id"] for item in items)


def test_post_item_missing_fields(client):
    """Test POST /items fails with 400 when required fields are missing."""
    incomplete_question = {
        "question": "Incomplete Question?",
        "option_a": "Option A",
        # missing option_b, option_c, option_d, answer
    }
    response = client.post(
        '/items',
        data=json.dumps(incomplete_question),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data


def test_post_item_invalid_answer(client):
    """Test POST /items fails with 400 when answer is not A, B, C, or D."""
    invalid_answer_question = {
        "question": "What is Grafana?",
        "option_a": "Data visualization platform",
        "option_b": "Database engine",
        "option_c": "Code compiler",
        "option_d": "Web browser",
        "answer": "Z"  # Invalid answer choice
    }
    response = client.post(
        '/items',
        data=json.dumps(invalid_answer_question),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "Answer must be one of: 'A', 'B', 'C', 'D'" in data["error"]


def test_post_item_empty_payload(client):
    """Test POST /items fails with 400 on empty or invalid JSON."""
    response = client.post(
        '/items',
        data="not a valid json",
        content_type='application/json'
    )
    assert response.status_code == 400


def test_metrics_endpoint(client):
    """Test GET /metrics returns Prometheus metric format."""
    response = client.get('/metrics')
    assert response.status_code == 200
    text_data = response.data.decode('utf-8')
    assert "flask_http_requests_total" in text_data
    assert "quizbank_questions_total" in text_data
