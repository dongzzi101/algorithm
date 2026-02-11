def solution(want, number, discount):
    answer = 0
    n = sum(number) 
    
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    for i in range(len(discount) - n + 1):
        cart = {}

        for j in range(i, i+n):
            cart[discount[j]] = cart.get(discount[j], 0) + 1

        if cart == want_dict:
            answer += 1

    return answer