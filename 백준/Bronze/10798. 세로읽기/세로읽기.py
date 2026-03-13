word_graph = []

for _ in range(5):
    word_graph.append(list(input()))

result = []

for x in range(15):  
    for y in range(5):
        if x < len(word_graph[y]):
            result.append(word_graph[y][x])

print("".join(result))