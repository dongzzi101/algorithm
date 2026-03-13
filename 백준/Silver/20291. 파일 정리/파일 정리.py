n = int(input())

extension_map = {}

for _ in range(n):
    name, extension = input().split(".")
    
    if extension in extension_map:
        extension_map[extension] += 1
    else:
        extension_map[extension] = 1

for extension in sorted(extension_map):
    print(extension, extension_map[extension])