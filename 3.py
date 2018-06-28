def solution(S):
    cantidades= []
    for val in S:
        cantidades.append(S.count(val))

    maximaCant= max(cantidades)
    valores=[]

    for ind, valor in enumerate(cantidades):
        if(valor==maximaCant):
            valores.append(S[ind])

    return min(valores)

print(solution([1,1,2,2,3,4,77,9,55]))