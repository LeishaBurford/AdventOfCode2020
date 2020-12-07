from pathlib import Path

customs_forms = [form.strip() for form in open('Day6/customs_forms.txt').read().split('\n\n')]
questions_answered = [len(set(group.replace('\n', ''))) for group in customs_forms ]
print("Part 1:", sum(questions_answered))

questions_answered = [group.split('\n') for group in customs_forms]
questions_answered_by_all = []
for group in questions_answered:
    questions = set(group[0])
    for person in group:
        questions = questions.intersection(set(person))
    questions_answered_by_all.append(len(questions))
# print(customs_forms)
# print(questions_answered_by_all)
print("Part 2:", sum(questions_answered_by_all))
