def solution(S, startIdx):
    if S[startIdx] != '[':
        return -1
    stack1=[]
    for i in range(startIdx, len(S)):
        if S[i]=='[':
            stack1.append(S[i])
        elif S[i]==']':
            stack1.pop()
        if len(stack1)==0:
            return i
    return -1


print(solution("[ABC[23]][89]",0))