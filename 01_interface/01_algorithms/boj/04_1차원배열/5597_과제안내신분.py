# https://www.acmicpc.net/problem/5597
students = [i for i in range(1, 31)]

for _ in range(28):
    student = int(input())
    students.remove(student)

print(students[0])
print(students[1])
