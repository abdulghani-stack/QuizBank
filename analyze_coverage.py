import json
from syllabus_data import SYLLABUS_STRUCTURE

with open('seed_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Count how many questions exist for every single topic in SYLLABUS_STRUCTURE
syl_topic_counts = {}
for s in SYLLABUS_STRUCTURE:
    sub = s['subject']
    syl_topic_counts[sub] = {}
    for m in s['modules']:
        m_num = m['module_number']
        syl_topic_counts[sub][m_num] = {}
        for t in m['topics']:
            # count questions in this sub & module with topic == t
            matches = [q for q in questions if q['subject'] == sub and q['module_number'] == m_num and (q.get('topic','').strip().lower() == t.strip().lower() or t.strip().lower() in q.get('topic','').strip().lower())]
            syl_topic_counts[sub][m_num][t] = len(matches)

# Total syllabus topics
total_syl_topics = sum(len(m['topics']) for s in SYLLABUS_STRUCTURE for m in s['modules'])
topics_with_questions = sum(1 for s in syl_topic_counts.values() for m in s.values() for t, c in m.items() if c > 0)
topics_without_questions = total_syl_topics - topics_with_questions

print(f"Total Syllabus Topics: {total_syl_topics}")
print(f"Syllabus Topics WITH matching questions in dataset: {topics_with_questions}")
print(f"Syllabus Topics WITHOUT matching questions in dataset: {topics_without_questions}")

# Distinct question topics in dataset
dataset_topics = set((q['subject'], q['module_number'], q['topic']) for q in questions)
print(f"Total distinct (Subject, Module, Topic) in 420 questions: {len(dataset_topics)}")
