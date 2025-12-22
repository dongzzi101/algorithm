result = []
for _ in range(10):
    num = int(input())
    result.append(num % 42)

answer = set(result)
print(len(answer))
