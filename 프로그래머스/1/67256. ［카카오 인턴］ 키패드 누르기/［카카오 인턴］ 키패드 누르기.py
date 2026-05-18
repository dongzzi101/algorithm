def solution(numbers, hand):
    answer = ''

    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    def calc_dist(pos, target):
        return abs(pos[0] - target[0]) + abs(pos[1] - target[1])

    left_pos = keypad['*']
    right_pos = keypad['#']

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_pos = keypad[number]

        elif number in [3, 6, 9]:
            answer += 'R'
            right_pos = keypad[number]

        else:
            target = keypad[number]

            left_dist = calc_dist(left_pos, target)
            right_dist = calc_dist(right_pos, target)

            if left_dist < right_dist:
                answer += 'L'
                left_pos = target

            elif left_dist > right_dist:
                answer += 'R'
                right_pos = target

            else:
                if hand == 'left':
                    answer += 'L'
                    left_pos = target
                else:
                    answer += 'R'
                    right_pos = target

    return answer