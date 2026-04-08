N, M = map(int, input().split())

no_hear_dict = {}
no_seen_dict = {}

for _ in range(N):
	name = input()
	if name in no_hear_dict:
		no_hear_dict[name] += 1
	else:
		no_hear_dict[name] = 0

for _ in range(M):
	name = input()
	if name in no_seen_dict:
		no_seen_dict[name] += 1
	else:
		no_seen_dict[name] = 0

no_hear_seen = []

for name in no_hear_dict:
    if name in no_seen_dict:
        no_hear_seen.append(name)

no_hear_seen.sort()

print(len(no_hear_seen))
for name in no_hear_seen:
    print(name)


