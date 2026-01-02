sound = input()

order = {'q':0, 'u':1, 'a':2, 'c':3, 'k':4}
states = []

for ch in sound:
    idx = order[ch]

    if idx == 0:
        if 4 in states:
            states[states.index(4)] = 0
        else:
            states.append(0)
    else:
        if idx - 1 in states:
            states[states.index(idx - 1)] = idx
        else:
            print(-1)
            exit()

if any(state != 4 for state in states):
    print(-1)
else:
    print(len(states))