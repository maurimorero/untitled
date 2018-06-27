def solution(A):
    B=sorted(A)
    mis=0
    band=0
    indice=0

    while band==0:
        if(B[indice]!=(indice+1)):
            mis=indice+1
            band=1
        indice=indice+1
    if mis==0:
        mis=len(B)
    return print(mis)



solution ([1,5,3,2])