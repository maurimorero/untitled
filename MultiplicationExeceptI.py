#There is an array A[N] of N numbers. You have to compose an array Output[N] such that Output[i] will be equal
# to multiplication of all the elements of A[N] except A[i]. For example Output[0] will be multiplication of A[1] to A[N-1] and
# Output[1] will be multiplication of A[0] and from A[2] to A[N-1]. Solve it without division operator and in O(n).

def solution(A):

    output=[]
    for indxA in range(len(A)):
        multi=1
        for indxB in range(len(A)):
            if (indxA!=indxB):
                multi= multi * A[indxB]
        output.append(multi)
    return output

print(solution([1,2,1,3,2]))
