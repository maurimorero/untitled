def solution(X, A):
    covered_time = [-1] * X  # Record the time, each position is covered
    #print(covered_time)
    uncovered = X  # Record the number of uncovered position

    for index in range(0, len(A)):
        print(A[index] - 1)
        if covered_time[A[index] - 1] != -1:
            # This position is already covered
            continue
        else:
            # This position is to be covered
            covered_time[A[index] - 1] = index
            uncovered -= 1
            if uncovered == 0:
                # All positions are covered
                return index

    # Finally, some positions are not covered
    return -1

solution(5,[1,3,1,4,2,3,5,4])

#A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0)
# and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

#You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one
# leaf falls at time K, measured in seconds.

#The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves
# appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1
# to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not
# change their positions once they fall in the river.