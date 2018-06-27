def solution(A):
    count=0
    firt=A[0]
    B= sorted(A)
    print(B)
    for idx in range(0,len(B)-1):
        if (B[idx]!=B[idx+1]):
            count+=1
    if (B[len(B)-1]!=B[len(B)-2]):
        count+=1
    return count

print (solution([2,1,1,2,3,1]))
