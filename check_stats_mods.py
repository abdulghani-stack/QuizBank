import json
with open('seed_questions.json', encoding='utf-8') as f:
    qs = json.load(f)

# Stats Mod 6 topics
mod6 = [q for q in qs if q.get('subject','').startswith('Statistics') and q.get('module_number') == 6]
topics = sorted(set(q.get('topic','') for q in mod6))
print('Stats Mod6 question topics:')
for t in topics:
    print(f'  {t}')

# Stats Mod 4 topics
mod4 = [q for q in qs if q.get('subject','').startswith('Statistics') and q.get('module_number') == 4]
topics4 = sorted(set(q.get('topic','') for q in mod4))
print()
print('Stats Mod4 question topics:')
for t in topics4:
    print(f'  {t}')
