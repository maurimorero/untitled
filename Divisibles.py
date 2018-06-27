# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    if (K==0):
       return 0
    cuenta=0

    for valor in range(A,B):
       #print (valor)
       #print (valor%K)
       if ((valor%K) ==0):
           cuenta+=1

    if(A==B):
        if ((A % K) == 0):
            cuenta += 1

    return (cuenta)

solution(6,6,2)