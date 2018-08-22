# Given a string s, write a function to check whether the opening/closing pairs and the order of the parentheses,
# brackets and curly-braces are correct in s, i.e they are balanced.

#The program should pass the following tests:

#assert is_balanced("[()]{a}{[(())]()}")
#assert not is_balanced("[(])")
#assert not is_balanced("(((]]]")
#assert not is_balanced("{[]")

#Add any additional tests that you feel are missing from the list of tests.

def checkBalance(S):

    stack = []

    for idx,char in enumerate(S):
        if char == '{' or char == '[' or char=='(':
            stack.append(char)
        else:
            if(len(stack) == 0):
                return 0
            lastStack= stack[-1]
            if char=='}' and lastStack=='{':
                stack.pop()
            elif char == ']' and lastStack=='[':
                stack.pop()
            elif char == ')' and lastStack=='(':
                stack.pop()

    if (len(stack) == 0):
        return 1
    else:
        return 0

print(checkBalance("[()]{a}{[(())]()}"))
print(checkBalance("[(])"))
print(checkBalance("(((]]]"))
print(checkBalance("{[]"))
print(checkBalance("{}}"))
