N, M = map(int, input().split())
train = [[0] * 20 for _ in range(N)]

for _ in range(M):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        _, train_num, seat = cmd
        train[train_num - 1][seat - 1] = 1

    elif cmd[0] == 2:
        _, train_num, seat = cmd
        train[train_num - 1][seat - 1] = 0

    elif cmd[0] == 3:
        _, train_num = cmd
        t = train_num - 1
        train[t] = [0] + train[t][:19]

    elif cmd[0] == 4:
        _, train_num = cmd
        t = train_num - 1
        train[t] = train[t][1:] + [0]

print(len(set(tuple(t) for t in train)))