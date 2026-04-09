

def include_vowel(word):
	

	for ch in word:
		if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
			return True
	return False

def three_in_a_row(word):
	const_count = 0
	vowel_count = 0

	for ch in word:
		if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
			vowel_count += 1
			const_count = 0
			
			if vowel_count == 3:
				return False
		
		else:
			const_count += 1
			vowel_count = 0

			if const_count == 3:
				return False

	return True

def two_in_a_row_except_e_and_o(word):
	same_o_e_count = 0

	prev = word[0]

	for i in range(1, len(word)):
		if prev == word[i]:
			if word[i] == "e" or word[i] == "o":
				same_o_e_count += 1
				if same_o_e_count == 2:
					return False
				prev = word[i]
			else:
				return False

		else:
			same_o_e_count = 0
			prev = word[i]

	return True






while True:
	word = input()
	if word == "end":
		break

	include_vowel_reuslt = include_vowel(word)

	# if not include_vowel_reuslt:
	# 	print(f"<{word}> is not acceptable.")

	three_in_a_row_result = three_in_a_row(word)

	# if not three_in_a_row_result:
	# 	print(f"<{word}> is not acceptable.")

	two_in_a_row_except_e_and_o_result = two_in_a_row_except_e_and_o(word)

	if include_vowel_reuslt and three_in_a_row_result and two_in_a_row_except_e_and_o_result:
		print(f"<{word}> is acceptable.")
	else:
		print(f"<{word}> is not acceptable.")
