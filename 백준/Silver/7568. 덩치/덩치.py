N = int(input())

peoples = []

for i in range(N):
    weight, height = map(int, input().split())
    peoples.append((weight, height))

rank = 1

for me in peoples:
    rank = 1
    for other in peoples:
        if me[0] < other[0] and me[1] < other[1]:
            rank +=1

    print(rank, end=" ")
