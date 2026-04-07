T = int(input())


for _ in range(T):
	word_map = {}
	s = input()

	for ch in s:
		if ch == ' ':
			continue
			
		if ch in word_map:
			word_map[ch] += 1
		else:
			word_map[ch] = 1

	max_value = max(word_map.values())

	max_keys = [k for k, v in word_map.items() if v == max_value]

	if len(max_keys) > 1:
		print("?")
	else:
		print(max_keys[0])

