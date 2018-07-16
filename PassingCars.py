def solution(A):
    east=[]
    passing=0
    for idx,car in enumerate(A):
        if(car==0):
            east.append(idx)

    for car in east:
        for idx, cars in enumerate(A):
            if (cars == 1) and (idx>car):
                passing+=1

    if passing>1000000000:
        return -1
    return passing

print ( solution([0,1,0,1,1]) )

#A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.
#Array A contains only 0s and/or 1s:
#0 represents a car traveling east,
#1 represents a car traveling west.
#The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east
# and Q is traveling to the west.

