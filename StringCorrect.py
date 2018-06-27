def solution():
    import re

    txt = 'First, solve the problem. Then, write the code. This is a test... And: another; test.'

    re1 = '.*?'  # Non-greedy match on filler
    re2 = '(?:[a-z][a-z0-9_]*)'  # Uninteresting: var
    re3 = '.*?'  # Non-greedy match on filler
    re4 = '((?:[a-z][a-z0-9_]*))'  # Variable Name 1

    rg = re.compile(re1 + re2 + re3 + re4, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m:
        var1 = m.group(1)
        print
        "(" + var1 + ")" + "\n"


#print(solution("     hola che esto es una. prueba"))