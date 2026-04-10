def solution(record):
    answer = []
    
    user_map = {}
    
    for line in record:
        cmd = line.split(" ")
        if cmd[0] != "Leave":
            user_map[cmd[1]] = cmd[2]
    
    
    for line in record:
        cmd = line.split(" ")
        if cmd[0] == "Enter":
            answer.append("%s님이 들어왔습니다." % user_map[cmd[1]])
        elif cmd[0] == "Leave":
            answer.append("%s님이 나갔습니다."% user_map[cmd[1]])
        else:
            pass
    
    return answer