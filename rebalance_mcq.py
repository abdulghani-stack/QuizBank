"""
Redistributes the correct answer position of seed_questions.json evenly across A, B, C, D (approx 105 each).
Validates that:
1. Every question retains its ID, question text, metadata, explanation, and correct answer content.
2. Correct answer keys are evenly distributed (A: ~105, B: ~105, C: ~105, D: ~105).
3. Every question has exactly 4 distinct options.
4. The key (A, B, C, D) exactly matches the original correct option text.
"""

import json
import random
import copy

def rebalance_dataset():
    with open('seed_questions.backup.json', 'r', encoding='utf-8') as f:
        original = json.load(f)

    total = len(original)
    print(f"Loaded {total} questions from backup.")
    assert total == 420, f"Expected 420 questions, got {total}"

    # Target: 105 of A, 105 of B, 105 of C, 105 of D
    # Generate deterministic cycle or pseudo-random balanced list with fixed seed
    target_keys = ['A', 'B', 'C', 'D'] * 105
    # Use deterministic shuffle with fixed seed for reproducibility
    rng = random.Random(42)
    rng.shuffle(target_keys)

    new_questions = []

    for i, orig_q in enumerate(original):
        q = copy.deepcopy(orig_q)
        target_ans = target_keys[i]

        # Extract original option values
        orig_ans_key = orig_q['answer'].upper()
        orig_options = {
            'A': orig_q['option_a'],
            'B': orig_q['option_b'],
            'C': orig_q['option_c'],
            'D': orig_q['option_d']
        }
        correct_text = orig_options[orig_ans_key]
        distractors = [orig_options[k] for k in ['A', 'B', 'C', 'D'] if k != orig_ans_key]

        # Assign options such that target_ans gets correct_text
        new_opts = {}
        new_opts[target_ans] = correct_text

        # Distribute the 3 distractors among the other 3 keys in order
        remaining_keys = [k for k in ['A', 'B', 'C', 'D'] if k != target_ans]
        for k_idx, rem_k in enumerate(remaining_keys):
            new_opts[rem_k] = distractors[k_idx]

        # Build updated question object
        q['option_a'] = new_opts['A']
        q['option_b'] = new_opts['B']
        q['option_c'] = new_opts['C']
        q['option_d'] = new_opts['D']
        q['answer'] = target_ans

        # Verify before appending
        # 1. Answer text in new object matches original correct text
        new_ans_key = q['answer']
        assert q[f"option_{new_ans_key.lower()}"] == correct_text, f"Mismatch at question id {q['id']}"
        # 2. Options are 4 distinct non-empty strings
        opts_list = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        assert len(set(opts_list)) == 4, f"Duplicate options at question id {q['id']}"
        assert all(len(o.strip()) > 0 for o in opts_list), f"Empty option at question id {q['id']}"

        new_questions.append(q)

    # Full dataset validation
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for q in new_questions:
        counts[q['answer']] += 1

    print("\nNew Answer Distribution:", counts)
    assert counts['A'] == 105
    assert counts['B'] == 105
    assert counts['C'] == 105
    assert counts['D'] == 105

    # Check that all IDs match
    orig_ids = [q['id'] for q in original]
    new_ids = [q['id'] for q in new_questions]
    assert orig_ids == new_ids, "Question IDs changed!"

    # Save to seed_questions.json
    with open('seed_questions.json', 'w', encoding='utf-8') as f:
        json.dump(new_questions, f, indent=2, ensure_ascii=False)

    print("Successfully wrote 420 rebalanced questions to seed_questions.json")

if __name__ == '__main__':
    rebalance_dataset()
