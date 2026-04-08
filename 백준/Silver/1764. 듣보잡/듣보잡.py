N, M = map(int, input().split())

no_hear = set(input() for _ in range(N))
no_seen = set(input() for _ in range(M))

result = sorted(no_hear & no_seen)

print(len(result))
for name in result:
	print(name)