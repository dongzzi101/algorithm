H, M = map(int, input().split())

if M < 45:
    H = (H-1) % 24
    M += 60

M -= 45

print(H, M)
