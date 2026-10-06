import pytest

from app import app


@pytest.fixture
def client():
    """Create a Flask test client for the application."""
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


@pytest.mark.parametrize(
    ("subject", "module", "topic", "expected_question_topic"),
    [
        (
            "Statistics for Machine Learning and Data Science",
            "4",
            "Precision",
            "Precision-Recall curves",
        ),
        (
            "Statistics for Machine Learning and Data Science",
            "4",
            "Recall",
            "Precision-Recall curves",
        ),
        (
            "Statistics for Machine Learning and Data Science",
            "1",
            "Types of data",
            "Types of data",
        ),
        ("Computer Network", "3", "ARP", "ARP"),
        (
            "Artificial Intelligence and Soft Computing",
            "4",
            "Fuzzy sets",
            "Fuzzy sets",
        ),
        (
            "Agile Software Development and DevOps",
            "1",
            "Burndown chart",
            "Burndown chart",
        ),
    ],
)
def test_topic_map_includes_matching_question_topics(
    client, subject, module, topic, expected_question_topic
):
    """Syllabus topics with matching questions include their question topics."""
    response = client.get("/api/topic-map")

    assert response.status_code == 200
    topic_map = response.get_json()
    assert expected_question_topic in topic_map[subject][module][topic]


def test_topic_map_keeps_genuinely_unmatched_syllabus_topics_empty(client):
    """A syllabus topic without a corresponding question topic has no matches."""
    response = client.get("/api/topic-map")

    assert response.status_code == 200
    topic_map = response.get_json()
    assert "F1-score" in topic_map[
        "Statistics for Machine Learning and Data Science"
    ]["4"]
    assert topic_map["Statistics for Machine Learning and Data Science"]["4"][
        "F1-score"
    ] == []
