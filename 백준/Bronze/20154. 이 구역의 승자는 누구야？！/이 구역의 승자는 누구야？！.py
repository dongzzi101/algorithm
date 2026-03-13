score = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]

s = input()

sum = 0
for ch in s:
	sum += score[ord(ch) - ord('A')]

print("I'm a winner!" if sum % 2 != 0 else "You're the winner?")