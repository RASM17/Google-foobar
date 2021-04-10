def findTop(h,node):
    maxInt = 2**h-1
    top = maxInt
    notFound = True
    height = h-1
    if(node > 0 and node <= maxInt):
        if top == node:
            return -1
        while(notFound):
            right= top-1
            level= ((2**height)-1)
            left= right-level

            if( node == left or node == right):
                return top
            if(node < left):
                top = left
                height -= 1
            if(node > left):
                top = right
                height -= 1
    return -2
    
def solution(h, q):
    result = []
    for i in q:
        result.append(findTop(h,i))
    return result

print(solution(3, [1, 4, 7]))
print(solution(3, [7, 3, 5, 1]))
print(solution(5, [19, 14, 28]))