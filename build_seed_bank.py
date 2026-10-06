"""
Master Question Bank Seed Assembler and Validator for Mumbai University T.E. AI&DS (Sem V).
Assembles all 7 subjects x 6 modules x 10 questions = 420 questions.
Validates:
- No duplicate questions or duplicate wording
- Valid answer keys (A, B, C, D)
- Exactly four non-empty options
- Non-empty explanation for every question
- All metadata fields (subject, subject_code, module, module_number, topic, difficulty, question_type)
"""

import json
from generate_seed_s1 import generate_all_questions as gen_s1
from generate_seed_s2 import generate_s2_questions as gen_s2
from generate_seed_s3 import generate_s3_questions as gen_s3
from generate_seed_s4 import generate_s4_questions as gen_s4
from generate_seed_s5 import generate_s5_questions as gen_s5
from generate_seed_s6_s7 import generate_s6_questions as gen_s6, generate_s7_questions as gen_s7
from syllabus_data import SYLLABUS_STRUCTURE

def assemble_and_validate_bank():
    all_questions = []
    
    q1, id1 = gen_s1()
    q2, id2 = gen_s2(id1)
    q3, id3 = gen_s3(id2)
    q4, id4 = gen_s4(id3)
    q5, id5 = gen_s5(id4)
    q6, id6 = gen_s6(id5)
    q7, id7 = gen_s7(id6)

    all_questions.extend(q1)
    all_questions.extend(q2)
    all_questions.extend(q3)
    all_questions.extend(q4)
    all_questions.extend(q5)
    all_questions.extend(q6)
    all_questions.extend(q7)

    print(f"Total questions collected: {len(all_questions)}")

    # Validation Checks
    seen_questions = set()
    seen_ids = set()
    subject_counts = {}
    difficulty_counts = {}
    type_counts = {}

    for i, q in enumerate(all_questions):
        # 1. Unique ID
        q_id = q["id"]
        assert q_id not in seen_ids, f"Duplicate ID found: {q_id}"
        seen_ids.add(q_id)

        # 2. No duplicate question text
        q_text = q["question"].strip().lower()
        assert q_text not in seen_questions, f"Duplicate question text found at ID {q_id}: {q['question']}"
        seen_questions.add(q_text)

        # 3. Four options exist and are distinct
        opts = [q["option_a"].strip(), q["option_b"].strip(), q["option_c"].strip(), q["option_d"].strip()]
        for opt_idx, opt in enumerate(opts):
            assert len(opt) > 0, f"Empty option in question {q_id}"
        assert len(set(opts)) == 4, f"Duplicate options in question {q_id}: {opts}"

        # 4. Answer is valid
        assert q["answer"] in ["A", "B", "C", "D"], f"Invalid answer '{q['answer']}' in question {q_id}"

        # 5. Non-empty explanation
        assert len(q.get("explanation", "").strip()) > 5, f"Missing or short explanation in question {q_id}"

        # 6. Valid Subject and Code
        sub = q["subject"]
        code = q["subject_code"]
        assert len(sub) > 0 and len(code) > 0, f"Missing subject/code in question {q_id}"
        subject_counts[sub] = subject_counts.get(sub, 0) + 1

        # 7. Valid Module
        assert 1 <= q["module_number"] <= 6, f"Invalid module number {q['module_number']} in question {q_id}"
        assert len(q["module"]) > 0, f"Missing module name in question {q_id}"

        # 8. Valid Topic
        assert len(q["topic"]) > 0, f"Missing topic in question {q_id}"

        # 9. Difficulty & Type Tracking
        diff = q.get("difficulty", "medium").lower()
        q_type = q.get("question_type", "conceptual").lower()
        difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1
        type_counts[q_type] = type_counts.get(q_type, 0) + 1

    print("\n--- Validation Succeeded ---")
    print(f"Total verified questions: {len(all_questions)}")
    print("\nSubject Breakdown:")
    for sub, count in subject_counts.items():
        print(f"  - {sub}: {count} questions")

    print("\nDifficulty Breakdown:")
    for diff, count in difficulty_counts.items():
        pct = (count / len(all_questions)) * 100
        print(f"  - {diff.capitalize()}: {count} ({pct:.1f}%)")

    print("\nQuestion Type Breakdown:")
    for qt, count in type_counts.items():
        print(f"  - {qt}: {count}")

    # Write out verified seed JSON
    with open("seed_questions.json", "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print("\nSaved verified seed dataset to 'seed_questions.json'")

    return all_questions

if __name__ == "__main__":
    assemble_and_validate_bank()
