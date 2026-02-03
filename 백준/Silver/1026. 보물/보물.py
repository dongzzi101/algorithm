N = int(input())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a = sorted(arr_a, key=lambda x : -x)
arr_b.sort()

ans = 0
for i in range(N):
	ans += arr_a[i] * arr_b[i]

print(ans) 