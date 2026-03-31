while True:
    sentence = input()

    if sentence == "END":
        break

    stack = []

    for ch in sentence:
    	stack.append(ch)
        
    while stack:
        print(stack.pop(), end='')

    print()