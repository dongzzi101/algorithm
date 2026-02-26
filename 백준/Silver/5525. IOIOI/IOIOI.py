N = int(input())
M = int(input())
S = input()


count = 0
answer = 0
i = 1

while i < M - 1:
	if S[i-1:i+2] == "IOI":
		count+=1
		i += 2
		if count >= N:
			answer += 1
	else:
		count = 0
		i += 1

print(answer)