def solution(S):
    cantidades= []
    for val in S:
        cantidades.append(S.count(val)) # mete todos las cantidades de cada elemento a un array

    maximaCant= max(cantidades)  # busca la cantidad máxima
    valores=[]

    for ind, valor in enumerate(cantidades):
        if(valor==maximaCant):
            valores.append(S[ind]) # agrega a un array auxiliar los valores de todos los máximos

    return min(valores) # retorna el menor

print(solution([1,1,2,2,3,4,77,9,55]))