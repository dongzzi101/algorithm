answer = []

while True:
    s = input()

    if s == "END":
        break

    answer.append(s[::-1])

for sen in answer:
    print(sen)




