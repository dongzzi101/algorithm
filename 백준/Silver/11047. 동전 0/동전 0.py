N, K = map(int, input().split())

coins = []

for i in range(N):
    coins.append(int(input()))

coins.reverse()

count = 0
for coin in coins:
    if K == 0:
        break

    usable = K // coin
    count += usable
    K -= coin * usable

print(count)
