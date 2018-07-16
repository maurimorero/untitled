def NumMasPopular(S, cantidad):
    if len(S)>5000: # si el array tiene mas de 5000 elementos, devuelvo 0
        return 0
    cantidades= []
    for val in S:
        cantidades.append(S.count(val)) # mete todos las cantidades de cada elemento a un array

    maximaCant= max(cantidades)  # busca la cantidad máxima
    valores=[]

    for ind, valor in enumerate(cantidades):
        if(valor==maximaCant):
            valores.append(S[ind]) # agrega a un array auxiliar los valores de todos los máximos

    return min(valores) # retorna el menor

print(NumMasPopular([1,1,2,2,2,3,4,77,77,77,77,9,55],13))