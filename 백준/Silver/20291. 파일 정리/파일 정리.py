N = int(input())

result = {}

for _ in range(N):
    fullname = input()
    ext = fullname.split(".")[-1]

    if ext in result:
        result[ext] += 1
    else:
        result[ext] = 1

for ext in sorted(result):
    print(ext, result[ext])
