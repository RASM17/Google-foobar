def solution(s):
    salute = 0
    my_dict = {}
    for index,i in enumerate(s):
        if i == '<' or i == '>':
            if not my_dict.get(i):
                my_dict[i] = [index]
            else:
                my_dict[i].extend([index])
    goingRight = my_dict.get('>')
    goingLeft = my_dict.get('<')
    j = 0
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