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

#You are given an array A consisting of N integers.

#For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the
# divisors of A[i]. We say that these elements are non-divisors.