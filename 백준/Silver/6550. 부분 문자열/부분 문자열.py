while True:
	try:
		s, t = input().split()
	except:
		break


	i = 0

	for ch in t:
		if i < len(s) and ch == s[i]:
			i += 1

	print("Yes" if len(s) == i else "No")
