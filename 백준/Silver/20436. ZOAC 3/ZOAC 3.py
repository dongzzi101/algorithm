import sys
input = sys.stdin.readline

keyboard = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]

pos = {}
for i in range(len(keyboard)):
    for j in range(len(keyboard[i])):
        pos[keyboard[i][j]] = (i, j)

left_keys = set("qwertasdfgzxcv")
right_keys = set("yuiophjklnm")

left_init, right_init = input().split()
targets = input().strip()

left = pos[left_init]
right = pos[right_init]

count = 0

for t in targets:
    target = pos[t]

    if t in left_keys:
        dist = abs(left[0] - target[0]) + abs(left[1] - target[1])
        count += dist + 1
        left = target

    else:  
        dist = abs(right[0] - target[0]) + abs(right[1] - target[1])
        count += dist + 1
        right = target

print(count)