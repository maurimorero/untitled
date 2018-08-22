def braces(values):
    responses=[]
    for val in values:
        if (checkBalance(val) ==1):
            responses.append("YES")
        elif (checkBalance(val) ==0):
            responses.append("NO")
    return responses

def checkBalance(S):
    stack = []
    for sign in S:
        if sign == '(' or sign == '[' or sign == '{':
            stack.append(sign)
        else:
            if len(stack) == 0:
                return 0
            stackLast = stack[-1]
            if sign == ')' and stackLast == '(':
                stack.pop()
            elif sign == ']' and stackLast == '[':
                stack.pop()
            elif sign == '}' and stackLast == '{':
                stack.pop()
            else:
                return 0

    if len(stack) == 0:
        return 1
    else:
        return 0


print(braces(['{[()]}','[[[](}']))