def comb(index, level):
    global choose, arr, n
    if level == 6:
        for i in choose:
            print(i, end=' ')
        print()
        return
    
    for i in range(index, n):
        choose.append(arr[i])
        comb(i+1, level+1)
        choose.pop()
    
while True:
    choose = []
    lst = list(map(int, input().split()))
    
    n = lst[0]
    arr = lst[1:]
    
    if n == 0:
        break
    comb(0,0)
    print()