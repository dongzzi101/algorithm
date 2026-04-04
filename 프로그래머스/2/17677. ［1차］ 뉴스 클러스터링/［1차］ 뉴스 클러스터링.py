def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    strA, strB = [], []
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalpha():
            strA.append(str1[i:i+2])
    
    for i in range(len(str2) - 1):
        if str2[i:i+2].isalpha():
            strB.append(str2[i:i+2])
    
    strB_copy = strB[:]
    count = 0
    
    for s in strA:
        if s in strB_copy:
            count += 1
            strB_copy.remove(s)
    
    total_count = len(strA) + len(strB) - count
    
    if total_count == 0:
        return 65536
    
    return int((count / total_count) * 65536)