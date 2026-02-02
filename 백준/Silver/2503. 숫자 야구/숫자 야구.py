from itertools import permutations

N = int(input())

infos = [input().split() for _ in range(N)]

ans = 0

for cur in permutations(range(1, 10), 3):
	ok = True

	for num, strike, ball in infos:
		real_strike = real_ball = 0

		for i in range(3):
			if str(cur[i]) == num[i]:
				real_strike += 1
			elif str(cur[i]) in num:
				real_ball += 1

		if real_strike != int(strike) or real_ball != int(ball):
			ok = False
			break

	if ok:
		ans +=1

print(ans)
