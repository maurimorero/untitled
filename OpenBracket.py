def checkBracket(S, finishIndex):
    if(S[finishIndex]!=']'):
        return -1
    stack=[]
    for idx in reversed(range(finishIndex+1)):
        if (S[idx]==']'):
            stack.append(S[idx])
        elif(S[idx]=='['):
            stack.pop()
            if(len(stack)==0):
                return idx

    return -1

print(checkBracket("[ABC[23]][89]",12))