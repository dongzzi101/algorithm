N = int(input())

def group_word(word):

	seen = set()
	prev = word[0]

	seen.add(prev)
	
	for i in range(1, len(word)):
		if prev != word[i]:
			if word[i] in seen:
				return 0
			seen.add(word[i])
			prev = word[i]

	return 1

count = 0
for _ in range(N):
	s = input()
	result = group_word(s)
	count += result

print(count)