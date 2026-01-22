S = input()
K = input()

filtered = []
for ch in S:
    if ch.isalpha():          
        filtered.append(ch)

filtered_S = ''.join(filtered)

if K in filtered_S:           
    print(1)
else:
    print(0)
