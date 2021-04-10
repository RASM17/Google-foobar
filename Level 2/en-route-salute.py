def solution(s):
    salute = 0
    goingLeft = []
    goingRight = []
    for index,i in enumerate(s):
        if i == '<':
            goingLeft.append(index)
        elif i == '>':
            goingRight.append(index)
    for i in goingRight:
        for j in goingLeft:
            if(i < j):
                salute += 1
            
    return salute*2

print(solution(">----<"))
print(solution("<<>><"))
print(solution("--->-><-><-->-"))
print(solution("-<-><-->-"))
print(solution("-<->><-->>-<<->->"))