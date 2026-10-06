"""
Verify that the /api/topic-map endpoint returns correct mappings
and that filtering works for previously-failing topics.
"""
import urllib.request
import json
import time

BASE = 'http://localhost:5000'

def fetch(path):
    with urllib.request.urlopen(BASE + path) as r:
        return json.loads(r.read().decode())

time.sleep(2)
print('=== Fetching topic-map and questions ===')
topic_map = fetch('/api/topic-map')
questions  = fetch('/items')
print(f'topic-map: {len(topic_map)} subjects')
print(f'questions: {len(questions)} total')
print()

def test_topic(subj, mod_str, topic):
    """Simulate the JS initializeQuiz fuzzy match for a syllabus topic."""
    pool = [q for q in questions if q.get('subject') == subj and q.get('module_number') == int(mod_str)]
    # Fast-path: use topic-map
    matched_q_topics = set()
    if subj in topic_map and mod_str in topic_map[subj]:
        aliases = topic_map[subj][mod_str].get(topic, [])
        matched_q_topics = set(aliases)
    if matched_q_topics:
        filtered = [q for q in pool if q.get('topic','') in matched_q_topics]
    else:
        # Fallback: substring match
        tl = topic.lower()
        filtered = [q for q in pool if tl in (q.get('topic','') or '').lower()
                                    or (q.get('topic','') or '').lower() in tl]
    return filtered

print('=== Testing known-problematic syllabus topics ===')
tests = [
    ('Statistics for Machine Learning and Data Science', '6', 'Calibration'),
    ('Statistics for Machine Learning and Data Science', '4', 'Precision'),
    ('Statistics for Machine Learning and Data Science', '4', 'Recall'),
    ('Statistics for Machine Learning and Data Science', '4', 'F1-score'),
    ('Statistics for Machine Learning and Data Science', '1', 'Types of data'),
    ('Computer Network', '3', 'ARP'),
    ('Artificial Intelligence and Soft Computing', '4', 'Fuzzy sets'),
    ('Agile Software Development and DevOps', '1', 'Burndown chart'),
]

all_pass = True
for subj, mod, topic in tests:
    result = test_topic(subj, mod, topic)
    aliases = []
    if subj in topic_map and mod in topic_map[subj]:
        aliases = topic_map[subj][mod].get(topic, [])
    status = 'PASS' if result else 'FAIL'
    if not result:
        all_pass = False
    print(f'  [{status}] Mod{mod}/{topic!r:30s} -> aliases={aliases} -> {len(result)} Qs')

print()
print('Coverage summary per subject:')
for subj, mods in topic_map.items():
    total = sum(len(topics) for topics in mods.values())
    mapped = sum(1 for topics in mods.values() for matches in topics.values() if matches)
    print(f'  {subj[:50]:50s}  {mapped}/{total} topics covered ({100*mapped//total}%)')

print()
print('OVERALL:', 'ALL PASS' if all_pass else 'SOME FAILURES - check above')
