def solution(X, Y, D):
    movs=0
    position=X
    if(X==Y):
        return 0
    while (position<Y):
        position=position+D
        movs=movs+1
    return movs