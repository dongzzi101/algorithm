N, K, B = map(int, input().split())

check = [0] * N

for _ in range(B):
	id = int(input())
	check[id - 1] = 1

psum = [0] * N

psum[0] = check[0]

for i in range(1, N):
	psum[i] = psum[i-1] + check[i]

count = []
for i in range(0, N-K+1):
	if i == 0:
		num = psum[i + K - 1]
	else:
		num = psum[i+K-1] - psum[i-1]

	count.append(num)

print(min(count))
