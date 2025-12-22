N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
result = 0
for i in range(N):
    result += (scores[i] / max_score) * 100

print(result / N)
