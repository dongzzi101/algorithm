N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

arr = sorted(arr, key=lambda x : (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]))

for b,p,q,r in arr[:3]:
    print(b, sep=' ')
    