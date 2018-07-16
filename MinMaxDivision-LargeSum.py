def blockSizeIsValid(A, max_block_cnt, max_block_size):
    block_sum = 0
    block_cnt = 0

    for element in A:
        if block_sum + element > max_block_size:
            block_sum = element
            block_cnt += 1
        else:
            block_sum += element
        if block_cnt >= max_block_cnt:
            return False

    return True


def binarySearch(A, max_block_cnt, using_M_will_give_you_wrong_results):
    lower_bound = max(A)
    upper_bound = sum(A)

    if max_block_cnt == 1:      return upper_bound
    if max_block_cnt >= len(A): return lower_bound

    while lower_bound <= upper_bound:
        candidate_mid = (lower_bound + upper_bound) // 2
        if blockSizeIsValid(A, max_block_cnt, candidate_mid):
            upper_bound = candidate_mid - 1
        else:
            lower_bound = candidate_mid + 1

    return lower_bound


def solution(K, M, A):
    return binarySearch(A, K, M)

#You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.
#You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every
# element of the array should belong to some block.
#The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.
#The large sum is the maximal sum of any block.
