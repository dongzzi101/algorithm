arr = []

for _ in range(9):
    arr.append(int(input()))

max_num = 0
max_index = 0

for i in range(len(arr)):

    if arr[i] > max_num:
        max_num = arr[i]
        max_index = i + 1

print(max_num)
print(max_index)
