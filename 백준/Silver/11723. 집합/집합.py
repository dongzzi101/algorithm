import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
bit = 0

for _ in range(N):
    cmd = input().split()
    op = cmd[0]

    if op == "add":
        x = int(cmd[1])
        bit |= (1 << (x - 1))

    elif op == "remove":
        x = int(cmd[1])
        bit &= ~(1 << (x - 1))

    elif op == "check":
        x = int(cmd[1])
        write("1\n" if (bit & (1 << (x - 1))) else "0\n")

    elif op == "toggle":
        x = int(cmd[1])
        bit ^= (1 << (x - 1))

    elif op == "all":
        bit = (1 << 20) - 1

    else: 
        bit = 0
