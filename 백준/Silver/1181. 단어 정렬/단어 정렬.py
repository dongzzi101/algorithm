n = int(input())


result = set()

for _ in range(n):
	result.add(input())

result = list(result)

result.sort(key=lambda x: (len(x), x))

for word in result:
    print(word)



