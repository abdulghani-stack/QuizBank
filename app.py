"""
Quiz Question Bank — Flask Backend
B1-G6 DevOps Academic Project REST API with In-Memory Storage

Endpoints:
- GET  /              -> Serve the QuizBank SaaS dashboard
- GET  /items         -> Retrieve all quiz questions
- POST /items         -> Add a new quiz question
- GET  /health        -> Health check endpoint
- GET  /metrics       -> Prometheus metrics endpoint
- GET  /api/topic-map -> Syllabus-to-question topic alias map
"""

import time
from flask import Flask, jsonify, request, render_template, Response
from prometheus_client import (
    Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
)

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Prometheus Metrics
# ---------------------------------------------------------------------------
REQUEST_COUNT = Counter(
    'flask_http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'http_status']
)

REQUEST_LATENCY = Histogram(
    'flask_http_request_duration_seconds',
    'HTTP request latency in seconds',
    ['method', 'endpoint']
)

QUESTIONS_GAUGE = Gauge(
    'quizbank_questions_total',
    'Total number of quiz questions in memory'
)

APP_INFO = Gauge(
    'quizbank_app_info',
    'Application metadata',
    ['version', 'app_name']
)
APP_INFO.labels(version='1.0.0', app_name='quiz-question-bank').set(1)


@app.before_request
def _start_timer():
    """Record the start time for every incoming request."""
    request._start_time = time.time()


@app.after_request
def _record_metrics(response):
    """Record Prometheus metrics after every response."""
    # Skip the /metrics endpoint itself to avoid recursion noise
    if request.path == '/metrics':
        return response

    latency = time.time() - getattr(request, '_start_time', time.time())
    endpoint = request.path
    method = request.method
    status = str(response.status_code)

    REQUEST_COUNT.labels(method=method, endpoint=endpoint, http_status=status).inc()
    REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(latency)

    return response


import json
import os
from syllabus_data import SYLLABUS_STRUCTURE, SUBJECT_CATEGORIES
from study_material_data import STUDY_MATERIAL, get_study_material_by_code, get_study_material_summary

# ---------------------------------------------------------------------------
# Pre-seeded In-Memory Question Store
# ---------------------------------------------------------------------------
def _load_initial_questions():
    seed_file = os.path.join(os.path.dirname(__file__), 'seed_questions.json')
    if os.path.exists(seed_file):
        try:
            with open(seed_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass

    # Fallback initial questions if seed file not yet built
    return [
        {
            "id": 1,
            "subject": "Statistics for Machine Learning and Data Science",
            "subject_code": "2015111",
            "module": "Module I - Statistical Foundations, Covariance, and Sampling",
            "module_number": 1,
            "topic": "Types of data",
            "question": "A dataset contains features: 'Customer ID', 'Credit Rating (AAA, AA, A)', 'Temperature in Celsius', and 'Transaction Amount ($)'. What is the correct classification for 'Credit Rating' and 'Temperature in Celsius' respectively?",
            "option_a": "Ordinal data and Interval data",
            "option_b": "Nominal data and Ratio data",
            "option_c": "Ordinal data and Ratio data",
            "option_d": "Nominal data and Interval data",
            "answer": "A",
            "explanation": "Credit rating has a clear ranking order without fixed numeric differences (Ordinal), while Celsius temperature has meaningful differences but an arbitrary zero point (Interval).",
            "difficulty": "medium",
            "question_type": "conceptual",
            "category": "Statistics for Machine Learning and Data Science"
        }
    ]

questions_db = _load_initial_questions()
next_id = max([q["id"] for q in questions_db] + [0]) + 1

# Set initial gauge
QUESTIONS_GAUGE.set(len(questions_db))


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route('/')
def index():
    """Serves the main QuizBank dashboard."""
    return render_template('index.html')


@app.route('/api/syllabus', methods=['GET'])
def get_syllabus():
    """Returns the complete University of Mumbai AI&DS Sem V syllabus structure."""
    return jsonify({
        "semester": "Semester V",
        "academic_year": "2026-27",
        "categories": SUBJECT_CATEGORIES,
        "subjects": SYLLABUS_STRUCTURE
    }), 200


@app.route('/api/study-material', methods=['GET'])
def get_study_materials():
    """Returns the summary list or full study material for all subjects."""
    include_full = request.args.get('full', 'false').lower() == 'true'
    if include_full:
        return jsonify(STUDY_MATERIAL), 200
    return jsonify(get_study_material_summary()), 200


@app.route('/api/study-material/<subject_code>', methods=['GET'])
def get_subject_study_material(subject_code):
    """Returns detailed study material theory and notes for a specific subject code."""
    data = get_study_material_by_code(subject_code)
    if not data:
        return jsonify({"error": f"Study material for subject code '{subject_code}' not found"}), 404
    return jsonify(data), 200


@app.route('/items', methods=['GET'])
def get_items():
    """Retrieves quiz questions stored in memory with optional filtering."""
    results = questions_db

    # Subject filter (exact or code)
    subject = request.args.get('subject')
    if subject:
        subject_str = str(subject).strip().lower()
        results = [q for q in results if str(q.get('subject', '')).strip().lower() == subject_str]

    subject_code = request.args.get('subject_code')
    if subject_code:
        code_str = str(subject_code).strip()
        results = [q for q in results if str(q.get('subject_code', '')).strip() == code_str]

    # Module filter (supports module_number e.g. 1 or 'Module 1')
    module = request.args.get('module')
    if module:
        module_str = str(module).strip().lower()
        # Check if digit
        if module_str.isdigit():
            mod_num = int(module_str)
            results = [q for q in results if q.get('module_number') == mod_num]
        else:
            results = [q for q in results if module_str in str(q.get('module', '')).lower() or module_str == str(q.get('module_number', ''))]

    module_number = request.args.get('module_number')
    if module_number:
        try:
            mod_num = int(module_number)
            results = [q for q in results if q.get('module_number') == mod_num]
        except ValueError:
            pass

    # Topic filter
    topic = request.args.get('topic')
    if topic:
        topic_str = str(topic).strip().lower()
        results = [q for q in results if topic_str in str(q.get('topic', '')).lower()]

    # Difficulty filter
    difficulty = request.args.get('difficulty')
    if difficulty:
        diff_str = str(difficulty).strip().lower()
        results = [q for q in results if str(q.get('difficulty', '')).strip().lower() == diff_str]

    # Question Type filter
    question_type = request.args.get('question_type')
    if question_type:
        qt_str = str(question_type).strip().lower()
        results = [q for q in results if str(q.get('question_type', '')).strip().lower() == qt_str]

    # Category filter (for legacy compatibility)
    category = request.args.get('category')
    if category:
        cat_str = str(category).strip().lower()
        results = [q for q in results if cat_str in str(q.get('category', '')).lower() or cat_str in str(q.get('subject', '')).lower()]

    return jsonify(results), 200


@app.route('/items', methods=['POST'])
def create_item():
    """Adds a new quiz question to the in-memory database."""
    global next_id

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid or missing JSON payload"}), 400

    # Validate mandatory core fields
    required_fields = ['question', 'option_a', 'option_b', 'option_c', 'option_d', 'answer']
    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return jsonify({"error": f"Field '{field}' is required and cannot be empty"}), 400

    # Validate answer choice
    answer = str(data['answer']).strip().upper()
    if answer not in ['A', 'B', 'C', 'D']:
        return jsonify({"error": "Answer must be one of: 'A', 'B', 'C', 'D'"}), 400

    # Extract or fallback syllabus fields
    subject = str(data.get('subject', data.get('category', 'General'))).strip() or 'General'
    subject_code = str(data.get('subject_code', '')).strip()
    module = str(data.get('module', '')).strip()
    module_number = data.get('module_number')
    if module_number is not None:
        try:
            module_number = int(module_number)
        except (ValueError, TypeError):
            module_number = None

    topic = str(data.get('topic', '')).strip()
    explanation = str(data.get('explanation', '')).strip()
    difficulty = str(data.get('difficulty', 'Medium')).strip().capitalize() or 'Medium'
    question_type = str(data.get('question_type', 'conceptual')).strip().lower() or 'conceptual'

    new_item = {
        "id": next_id,
        "question": str(data['question']).strip(),
        "option_a": str(data['option_a']).strip(),
        "option_b": str(data['option_b']).strip(),
        "option_c": str(data['option_c']).strip(),
        "option_d": str(data['option_d']).strip(),
        "answer": answer,
        "explanation": explanation,
        "subject": subject,
        "subject_code": subject_code,
        "module": module,
        "module_number": module_number,
        "topic": topic,
        "category": subject,  # Legacy backwards compatibility
        "difficulty": difficulty,
        "question_type": question_type
    }

    next_id += 1
    questions_db.append(new_item)
    QUESTIONS_GAUGE.set(len(questions_db))

    return jsonify(new_item), 201


@app.route('/api/topic-map', methods=['GET'])
def get_topic_map():
    """Returns a mapping from syllabus topics to matching question topics.
    
    For each syllabus topic, returns the list of question topics that match it
    (via exact match, substring containment, or significant token overlap).
    This enables reliable frontend filtering without hard-coded aliases.
    """
    import re

    def _normalize(s):
        """Lowercase, strip punctuation, split into tokens."""
        return set(re.findall(r'[a-z0-9]+', s.lower()))

    # Collect all unique question topics for each (subject, module_number) pair
    q_topics_by_submod = {}  # (subject, module_number) -> [topic_string, ...]
    for q in questions_db:
        key = (q.get('subject', ''), q.get('module_number', 0))
        qt = q.get('topic', '').strip()
        if qt:
            q_topics_by_submod.setdefault(key, set()).add(qt)

    # Common stop-words to ignore when comparing tokens
    STOP = {'and', 'or', 'of', 'the', 'in', 'for', 'a', 'an', 'to', 'with', 'on', 'by'}

    def _topics_match(syllabus_topic, question_topic):
        """Return True if syllabus_topic is semantically related to question_topic."""
        st = syllabus_topic.strip()
        qt = question_topic.strip()

        # 1. Exact match (case-insensitive)
        if st.lower() == qt.lower():
            return True

        # 2. Either is a substring of the other (case-insensitive)
        stl, qtl = st.lower(), qt.lower()
        if stl in qtl or qtl in stl:
            return True

        # 3. Significant token overlap (ignoring stop-words, min 1 meaningful shared token)
        st_tokens = _normalize(st) - STOP
        qt_tokens = _normalize(qt) - STOP
        if st_tokens and qt_tokens and len(st_tokens & qt_tokens) >= 1:
            # Require shared tokens to be at least 3 chars to avoid noise (e.g. 'a', 'k')
            meaningful_shared = {t for t in (st_tokens & qt_tokens) if len(t) >= 3}
            if meaningful_shared:
                return True

        return False

    # Build the map: for each subject → {module_number → {syllabus_topic → [matching_q_topics]}}
    result = {}
    for subj_data in SYLLABUS_STRUCTURE:
        subject = subj_data['subject']
        result[subject] = {}
        for mod in subj_data.get('modules', []):
            mod_num = mod['module_number']
            q_topics_for_mod = q_topics_by_submod.get((subject, mod_num), set())
            topic_matches = {}
            for syl_topic in mod.get('topics', []):
                matched = [qt for qt in q_topics_for_mod if _topics_match(syl_topic, qt)]
                topic_matches[syl_topic] = matched
            result[subject][mod_num] = topic_matches

    return jsonify(result), 200


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint to report API status."""
    return jsonify({"status": "OK"}), 200


@app.route('/metrics', methods=['GET'])
def metrics():
    """Prometheus metrics endpoint."""
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
