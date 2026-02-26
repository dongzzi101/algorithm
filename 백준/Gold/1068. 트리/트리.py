N = int(input())
parent = list(map(int, input().split()))
target = int(input())

tree = [[] for _ in range(N)]
root = 0

for i in range(N):
    if parent[i] == -1:
        root = i
    else:
        tree[parent[i]].append(i)


if target == root:
    print(0)
else:
    stack = [target]
    removed = set()

    while stack:
        node = stack.pop()
        removed.add(node)
        for child in tree[node]:
            stack.append(child)

    count = 0
    for i in range(N):
        if i in removed:
            continue
        if i == root or parent[i] not in removed:
            if len([c for c in tree[i] if c not in removed]) == 0:
                count += 1

    print(count)