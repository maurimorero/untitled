def solution(N):
    binario = bin(N)[2:]
    print (str(binario))
    cantidad=0
    gap=0
    gaps=[]
    for numero in (binario):
        if (numero=='0'):
            gap=gap+1
        else:
            gaps.append(gap)
            gap=0
    return print(max(gaps))

solution(1041)