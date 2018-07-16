# Name: Fish
# Link: https://codility.com/demo/take-sample-test/fish/


def solution(A, B):
    N = len(A)
    # The direction of the last fish
    direction = 0
    # The index of the last fish going downstream
    last_downstream = 0
    # Holds the number of alive fishes going upstream
    upstream = 0
    # Holds the alive fishes going from downstream
    downstream = stack(N)

    for k in range(N):
        # If the last fish is going upstream, this means that there is no fish before it going downstream
        if B[k] == 0 and direction == 0:
            upstream += 1
        # The fish k is going on the oposite direction of the last fish going downstream
        elif B[k] == 0 and direction == 1:
            # If the fish going downstream is bigger, then it eats the smaller fish and keep going
            if A[last_downstream] > A[k]:
                continue
            # Otherwise the other fish eats the one going downstream
            else:
                # We add the new fish to the ones going upstream
                upstream += 1
                # Update the direction of the last fish
                direction = 0

                # If there is more fishes going downstream we compare the sizes
                while downstream.size > 0:
                    head = downstream.pop()

                    # If there is a bigger fish going downstream, we subtract one from the result and change the direction
                    if A[k] < head:
                        downstream.push(head)
                        direction = 1
                        upstream -= 1
                        break
        # If fish is going downstream update the direction and push it to the stack
        elif B[k] == 1:
            direction = 1
            last_downstream = k
            downstream.push(A[k])

    # The result is the fishes going upstream plus the ones goind downstream
    return upstream + downstream.size


# Stack implementation
class stack(object):
    def __init__(self, N):
        self.size = 0
        self._stack_ = [0] * N

    def push(self, x):
        self._stack_[self.size] = x
        self.size += 1

    def pop(self):
        self.size -= 1
        return self._stack_[self.size]


#You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river,
# ordered downstream along the flow of the river.

#The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q.
# Initially, each fish has a unique position.

#Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array
# B contains the directions of the fish. It contains only 0s and/or 1s, where:

#0 represents a fish flowing upstream,
#1 represents a fish flowing downstream.
#If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other.
# Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

#If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
#If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
#We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to
# calculate the number of fish that will stay alive.