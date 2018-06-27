def solution(S):
  stack = []
  for sign in S:
    if sign == '(' or sign == '[' or sign =='{':
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

  return 1 if len(stack) == 0 else 0