N, M = map(int, input().split())

arr = list(map(int, input().split()))

negative = []
positive = []

for x in arr:
	if x > 0:
		positive.append(x)
	else:
		negative.append(-x)


positive = sorted(positive)[::-1]
negative = sorted(negative)[::-1]


dis = []

for pos in positive[::M]:
	dis.append(pos)

for neg in negative[::M]:
	dis.append(neg)

ans = 2 * sum(dis) - max(dis)
print(ans)