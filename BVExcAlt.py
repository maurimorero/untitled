def getIndex(s, i):
    if s[i] != '[':
        return -1
    d = []
    for k in range(i, len(s)):
        if s[k] == '[':
            d.append(s[i])
        elif s[k] == ']':
            d.pop()

        if len(d)==0:
            return k

    return -1

print(getIndex("[ABC[23]][89]",9))