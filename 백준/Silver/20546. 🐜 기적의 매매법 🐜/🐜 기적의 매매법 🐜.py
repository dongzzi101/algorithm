cash = int(input())
arr = list(map(int, input().split()))

jh, sm = cash, cash
jh_quantity, sm_quantity = 0, 0

for i in range(len(arr)):

    if jh >= arr[i]:
        quantity = jh // arr[i]
        jh_quantity += quantity
        jh -= quantity * arr[i]

    if i >= 3:
        if arr[i-3] < arr[i-2] < arr[i-1]:
            sm += sm_quantity * arr[i]
            sm_quantity = 0

        elif arr[i-3] > arr[i-2] > arr[i-1]:
            quantity = sm // arr[i]
            sm_quantity += quantity
            sm -= quantity * arr[i]
            
jh_total = (jh_quantity * arr[-1]) + jh
sm_total = (sm_quantity * arr[-1]) + sm

if jh_total > sm_total:
	print("BNP")
elif jh_total < sm_total:
	print("TIMING")
else:
	print("SAMESAME")
