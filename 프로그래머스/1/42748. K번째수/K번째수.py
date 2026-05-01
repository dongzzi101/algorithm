def solution(array, commands):
    answer = []
    
    
    for command in commands:
        start, end, target = command
        print(f"start = {start}, end = {end}, target = {target}")
        new_array = array[start-1:end]
        print(new_array)
        new_array.sort()
        answer.append(new_array[target-1])
        print(f"sorted_array : {new_array}  target : {new_array[target-1]}")
        array = array
    
    return answer