N = int(input())
cards = list(map(int, input().split()))

M = int(input())
arr = list(map(int, input().split()))

cards.sort()

def is_exist(target):
    left = 0
    right = len(cards) - 1

    while left <= right:
        mid = (left + right) // 2

        if target < cards[mid]:
            right = mid - 1
        elif target > cards[mid]:
            left = mid + 1
        else:
            return 1

    return 0

answer = []
for num in arr:
	answer.append(is_exist(num))

print(*answer)
