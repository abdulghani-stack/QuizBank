import json
from syllabus_data import SYLLABUS_STRUCTURE

with open('seed_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# For S1 M6:
m6_qs = [q for q in questions if q['subject_code'] == '2015111' and q['module_number'] == 6]
print('S1 M6 Question topics in dataset:')
for q in m6_qs:
    print(f'  ID {q["id"]}: topic="{q["topic"]}", question="{q["question"][:60]}..."')

s1_m6_syl = [m for m in SYLLABUS_STRUCTURE[0]['modules'] if m['module_number'] == 6][0]
print('\nS1 M6 Syllabus topics:')
print(' ', s1_m6_syl['topics'])
