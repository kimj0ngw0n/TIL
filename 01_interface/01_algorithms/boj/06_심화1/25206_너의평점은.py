# https://www.acmicpc.net/problem/25206
grades = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

total_score = 0
total_grade = 0

for _ in range(20):
    name, score, grade = input().split()
    score = float(score)

    if grade != 'P':
        total_score += score
        total_grade += score * grades[grade]

if total_grade:
    print(round(total_grade/total_score, 6))
else:
    print(format(0, '.6f'))
