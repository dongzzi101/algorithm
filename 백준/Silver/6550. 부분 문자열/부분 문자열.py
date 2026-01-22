import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    k, s = line.split()

    i = 0
    for ch in s:
        if i < len(k) and ch == k[i]:
            i +=1

    if i == len(k):
        print("Yes")
    else:
        print("No")
