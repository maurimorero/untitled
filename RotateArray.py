def solution(A, K):
    for i in range(K):
        aux=A.pop()
        A.insert(0, aux)
    return (A)

solution ([0,1,3,4],2)
