def solution(A):
    counts=[]
    B=A

    for value in A:
        count=0
        for div in B:
            if ((value%div)!=0):
                count +=1

        counts.append(count)

    return counts

print(solution([3,1,2,3,6]))