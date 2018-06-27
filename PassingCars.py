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



