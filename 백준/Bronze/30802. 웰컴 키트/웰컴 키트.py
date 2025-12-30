N = int(input())
arr = list(map(int, input().split()))
T, P = map(int, input().split())

t_count = 0
for x in arr:
    t_count += x // T
    if x % T != 0:
        t_count += 1

p_bundle = N // P
p_single = N % P

print(t_count)
print(p_bundle, p_single)
