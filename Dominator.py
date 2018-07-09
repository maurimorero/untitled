def solution(A):
    halfsize = len(A)//2

    for ind,val in enumerate(A):
        if A.count(val)>halfsize:
            return ind

    return -1

print((solution(['2','1','2','2','1','1','2','2'])))