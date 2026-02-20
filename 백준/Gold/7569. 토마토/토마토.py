from collections import deque

def bfs():
    q = deque()
    visit = [[[0] * M for _ in range(N)] for _ in range(H)]

    cnt = 0  

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:
                    q.append((h, i, j))
                    visit[h][i][j] = 1
                elif arr[h][i][j] == 0:
                    cnt += 1

    if cnt == 0:
        return 0

    max_day = 0

    while q:
        ch, ci, cj = q.popleft()

        for dh, di, dj in ((0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,0,0),(1,0,0)):
            nh = ch + dh
            ni = ci + di
            nj = cj + dj

            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M:
                if not visit[nh][ni][nj] and arr[nh][ni][nj] == 0:
                    q.append((nh, ni, nj))
                    visit[nh][ni][nj] = visit[ch][ci][cj] + 1
                    max_day = max(max_day, visit[nh][ni][nj])
                    cnt -= 1

    if cnt == 0:
        return max_day - 1
    else:
        return -1


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(bfs())