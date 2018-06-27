def solution(A):
    aux= sorted(A)
    print (aux)
    aux.reverse()
    return (aux[0]*aux[1]*aux[2])

print (solution([-3,1,2,-2,5,6]))