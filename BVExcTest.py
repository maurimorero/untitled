def checkBracket(S):
    if(S[0]!='['):
        return -1
    stack=[]
    for val in S:
        if (val=='[') or (val=='(') or (val=='{') :
            stack.append(val)
        elif (val==']') or (val==')') or (val=='}') :
            preVal=stack[-1]
            if(preVal=='[')and (val==']'):
                stack.pop()
            elif (preVal == '(') and (val == ')'):
                stack.pop()
            elif (preVal == '{') and (val == '}'):
                stack.pop()
            else:
                return 0
    if(len(stack)==0):
        return 1
    else:
        return 0

print (checkBracket('[(){}]'))