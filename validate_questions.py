"""
Detailed validation script comparing backup questions vs newly balanced seed_questions.json
"""
import json

def validate_rebalance():
    with open('seed_questions.backup.json', 'r', encoding='utf-8') as f:
        orig = json.load(f)
    with open('seed_questions.json', 'r', encoding='utf-8') as f:
        new = json.load(f)

    assert len(orig) == len(new) == 420, f"Count mismatch: {len(orig)} vs {len(new)}"

    errors = []
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    for i in range(420):
        o = orig[i]
        n = new[i]
        
        # ID must match
        if o['id'] != n['id']:
            errors.append(f"ID mismatch at index {i}: orig {o['id']} vs new {n['id']}")
        
        # Question text must match
        if o['question'] != n['question']:
            errors.append(f"Question text changed at ID {o['id']}")
            
        # Metadata must match
        for field in ['subject', 'subject_code', 'module', 'module_number', 'topic', 'difficulty', 'question_type', 'explanation']:
            if o.get(field) != n.get(field):
                errors.append(f"Field {field} changed at ID {o['id']}")
                
        # Correct answer key in new must match original correct option text
        orig_ans_key = o['answer'].lower()
        orig_correct_text = o[f'option_{orig_ans_key}']
        
        new_ans_key = n['answer'].lower()
        new_correct_text = n[f'option_{new_ans_key}']
        
        if orig_correct_text != new_correct_text:
            errors.append(f"Correct answer content corrupted at ID {o['id']}: orig '{orig_correct_text}' vs new '{new_correct_text}'")
            
        # Options must be a permutation of original options
        orig_opts_set = {o['option_a'], o['option_b'], o['option_c'], o['option_d']}
        new_opts_set = {n['option_a'], n['option_b'], n['option_c'], n['option_d']}
        if orig_opts_set != new_opts_set:
            errors.append(f"Option set mismatch at ID {o['id']}")
            
        counts[n['answer']] += 1

    print(f"Validation Errors: {len(errors)}")
    if errors:
        for e in errors[:10]:
            print(" -", e)
        raise ValueError("Validation failed")
    
    print("ALL 420 QUESTIONS PASSED FULL CONTENT & KEY INTEGRITY VALIDATION!")
    print("Answer counts:", counts)

if __name__ == '__main__':
    validate_rebalance()
