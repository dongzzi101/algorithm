S = input()
K = input()

result = ""
for ch in S:
	if ch.isdigit():
		continue
	
	result += ch


print("1" if K in result else "0")
