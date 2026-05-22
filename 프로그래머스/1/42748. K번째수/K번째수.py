def solution(array, commands):
    answer = []
    
    for command in commands:
        start, end, target = command
        print(f"start = {start}, end={end}, target={target}")
        cutting_array = array[start-1:end]
        sorted_array = sorted(cutting_array)
        answer.append(sorted_array[target-1])
    
    return answer