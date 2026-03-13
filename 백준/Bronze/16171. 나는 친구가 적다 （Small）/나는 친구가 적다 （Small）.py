s = input()
k = input()

words = []
for i in range(len(s)):
	if not s[i].isdigit():
		words.append(s[i])

words = ''.join(words)

if k in words:
	print(1)
else:
	print(0)
