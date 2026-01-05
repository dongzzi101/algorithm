import sys

N, M = map(int, input().split())

name_to_num = {}
num_to_name = {}

for i in range(1, N + 1):
    name = input().strip()
    name_to_num[name] = i
    num_to_name[i] = name

for _ in range(M):
    find = input().strip()

    if find.isdigit():
        print(num_to_name[int(find)])
    else:
        print(name_to_num[find])
