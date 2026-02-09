import sys

n = int(input())
nn = int(input())
adjs = [[] for _ in range(n + 1)]
"""
[
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]
"""
for _ in range(nn):
    a, b = map(int, input().split())
    adjs[a].append(b)
    adjs[b].append(a)

# print(adjs)
stack = [1]
visited = set()
while stack:
    node = stack.pop()
    # print(node)
    if node not in visited:
        visited.add(node)
        for adj in adjs[node]:
            if adj not in visited:
                stack.append(adj)
print(len(visited) - 1)