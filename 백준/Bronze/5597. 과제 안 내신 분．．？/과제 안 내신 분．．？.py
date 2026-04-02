from collections import defaultdict

student_map = defaultdict(int)

for _ in range(28):
    n = int(input())
    student_map[n] -= 1

for i in range(1, 31):
    if student_map[i] == 0:
        print(i)



