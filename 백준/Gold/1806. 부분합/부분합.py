N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
current_sum = 0
min_len = N + 1

while True:
    if current_sum >= S:
        min_len = min(min_len, end - start)
        current_sum -= arr[start]
        start += 1

    elif end == N:
        break

    else:
        current_sum += arr[end]
        end += 1

if min_len == N + 1:
    print(0)
else:
    print(min_len)