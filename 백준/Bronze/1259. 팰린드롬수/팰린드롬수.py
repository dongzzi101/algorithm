while True:
    test_case = input()

    if test_case == "0":
        break

    if test_case == test_case[::-1]:
        print("yes")
    else:
        print("no")
