N = int(input())

tips = []
for _ in range(N):
	tips.append(int(input()))

tips.sort(reverse=True)

total = 0

for i in range(len(tips)):
	money =  tips[i] - i

	if money > 0:
		total += money

print(total)



