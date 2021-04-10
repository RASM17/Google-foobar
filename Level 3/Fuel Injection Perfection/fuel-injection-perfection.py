def solution(n):
    n = int(n)
    steps = 0
    while( n>1):
        if(n % 2 == 0):
            n=n/2
        else:
            # Bit manipulation to obtain as many 0
            if(n == 3 or n % 4 == 1):
                n -= 1
            else:
                n += 1
        steps+=1
    return steps


print(solution(4))
print(solution(15))