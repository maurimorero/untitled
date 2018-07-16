def solution(X, Y, D):
    movs=0
    position=X
    if(X==Y):
        return 0
    while (position<Y):
        position=position+D
        movs=movs+1
    return movs

#A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get
# to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

#Count the minimal number of jumps that the small frog must perform to reach its target.
