A, B, C, D = map(int, input().split())

result = []


result.append(A)
result.append(B)
result.append(C)
result.append(D)

result.sort()

sum_first_team = 0
sum_second_team = 0

sum_first_team += (result[0] + result[3])
sum_second_team += (result[1] + result[2])

ans = abs(sum_first_team - sum_second_team)
print(ans)
