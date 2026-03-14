t = int(input())

for _ in range(t):
	stack = []
	vps = input()

	for ch in vps:
		if ch == "(":
			stack.append(ch)

		else:
			if len(stack) == 0:
				print("NO")
				break
			else:
				stack.pop()

	else:
		print("YES" if len(stack) == 0 else "NO")


