N, M = map(int, input().split())

names = set()
for _ in range(N):
    names.add(input())

result = []
for _ in range(M):
    name = input()
    if name in names:
        result.append(name)

result.sort()

print(len(result))

for i in result:
    print(i)


