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

def solution1 (A):
    if(len(A)==0):
        return 0
    count=0
    B=sorted(A)
    for ind,valor in enumerate(B):
        if (ind!=(len(B)-1)):
            if (B[ind] != B[ind + 1]):
                count += 1
    count+=1
    return count

print (solution1([2,1,1,2,3,1,4,5,5,5,5,5,5,5,6,97988,0]))

#Write a function
#def solution(A)
#that, given an array A consisting of N integers, returns the number of distinct values in array A.
#Assume that:
#N is an integer within the range [0..100,000];
#each element of array A is an integer within the range [−1,000,000..1,000,000].
