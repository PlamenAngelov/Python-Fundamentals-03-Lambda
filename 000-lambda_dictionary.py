student_grades = {
    'bob': [2, 2],
    'petar': [5, 2, 5],
    'maria': [6, 6, 5, 6],
    'alex': [2, 2]
}

key_sorted_grades = sorted(student_grades.items(), key=lambda kvp: kvp[0])
len_grades_sorted = sorted(student_grades.items(), key=lambda kvp: len(kvp[1]))
len_grades_key_sorted = sorted(student_grades.items(), key=lambda kvp: (len(kvp[1]), kvp[0]))
key_len_grades_sorted = sorted(student_grades.items(), key=lambda kvp: (kvp[0], len(kvp[1])))
len_grades_key_desc_sorted = sorted(student_grades.items(), key=lambda kvp: (len(kvp[1]), kvp[0]), reverse=True)
key_len_grades_desc_sorted = sorted(student_grades.items(), key=lambda kvp: (kvp[0], len(kvp[1])), reverse=True)

for name, grades in key_sorted_grades:
    print('{}: {}'.format(name, grades))

print("="*20)
for name, grades in len_grades_sorted:
    print('{}: {}'.format(name, grades))

print("="*20)
for name, grades in len_grades_key_sorted:
    print('{}: {}'.format(name, grades))

print("="*20)
for name, grades in key_len_grades_sorted:
    print('{}: {}'.format(name, grades))

print("="*20)
for name, grades in len_grades_key_desc_sorted:
    print('{}: {}'.format(name, grades))

print("="*20)
for name, grades in key_len_grades_desc_sorted:
    print('{}: {}'.format(name, grades))