def solution(data, n):
    my_dict = {}
    lista = list(data)
    if len(lista) < 100:
        for index,i in enumerate(lista):
            my_dict[i] = my_dict.get(i,0) +1
            if my_dict.get(i) > n:
                lista = list(filter(lambda a: a != i ,lista))
    return lista
    
print(solution([1, 2, 3], 0))
print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
print(solution([1, 2, 3], 6))
print(solution([5, 10, 15, 10, 7], 1))