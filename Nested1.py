# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    stack1=[]
    for val in S:
        if val=='(':
            stack1.append(val)
        elif val==')':
            if(len(stack1)==0):
                return 0
            elif (stack1.pop()!='('):
                return 0
    if (len(stack1)==0):
        return 1
    else:
        return 0


print(solution("(()(())())"))

