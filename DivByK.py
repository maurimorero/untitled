def solution(A, B, K):
    count=0
    for valor in range(A,(B+1)):
        print (valor)
        if ((valor%K)==0):
            count +=1
    return count
print (solution(6,10,2))