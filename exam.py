def solution(A):
    values =[]
    #print (max(A))
    values.append (3)
    for k in range (0, len(A)):
        auxArray1= A[0:k+1]

        auxArray2= A[k:len(A)]
        difference=max(auxArray1)-max(auxArray2)
        values.append(abs(difference))
    return max(values)


print(solution ([1, 3, -3]))