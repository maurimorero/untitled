# Assumption:
# - As an array can have more than one matching pairs, it will be returned the last one found (according with the statement)
# - If there is no matching pairs, it will be return 0
def lookForFisrtMatchingPair(A, sum):

    l = 0
    r = len(A) - 1
    matchingPairs= []
    while l < r:
        if (A[l] + A[r] == sum):
            matchingPairs.append([A[l],A[r]])
            r -= 1
        elif (A[l] + A[r] < sum):
            l += 1
        else:
            r -= 1
    if not matchingPairs:
        return 0
    else:
        return matchingPairs[-1]



print(lookForFisrtMatchingPair([2,3,6,7], 9))
print(lookForFisrtMatchingPair([1,3,3,7], 9))
print(lookForFisrtMatchingPair([], 9))
print(lookForFisrtMatchingPair([1,1,1,1,1,2,3,6,7], 9))
print(lookForFisrtMatchingPair([1,1,1,20,23,25,30], 50))