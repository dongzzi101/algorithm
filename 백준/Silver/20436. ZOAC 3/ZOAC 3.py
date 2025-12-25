keyboard = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]

pos = {}
for r in range(len(keyboard)):
    for c in range(len(keyboard[r])):
        pos[keyboard[r][c]] = (r, c)

left_only = set("qwertasdfgzxcv")
right_only = set("yuiophjklnm")

left_hand, right_hand = input().split()
word = input()

left_pos = pos[left_hand]
right_pos = pos[right_hand]

time = 0

for ch in word:
    target = pos[ch]

    if ch in left_only:
        dist = abs(left_pos[0] - target[0]) + abs(left_pos[1] - target[1])
        time += dist + 1
        left_pos = target
    else:
        dist = abs(right_pos[0] - target[0]) + abs(right_pos[1] - target[1])
        time += dist + 1
        right_pos = target

print(time)
