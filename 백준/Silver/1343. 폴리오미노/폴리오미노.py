s = input()

parts = s.split('.')
results = []

for p in parts:
	n = len(p)
	if n % 2 == 1:
		print(-1)
		exit()
	block = 'AAAA' * (n // 4)
	if n % 4 == 2:
		block += 'BB'
	results.append(block)

print('.'.join(results))