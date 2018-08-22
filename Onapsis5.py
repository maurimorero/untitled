# Complete the longestChain function below.
def longestChain(words):
    if(len(words)>50000):
        return -1
    counts=[]
    for word in words:
        counts.append(recursive(words,word,1))
    return max(counts)

def recursive(words,S,sum):
    position = 0
    leng = len(S)
    while (leng > 0):
        subword = S[0:position] + S[position + 1:]
        #print(subword)
        position += 1
        leng -= 1
        if (words.count(subword) > 0):
            return recursive(words,subword,sum+1)
    return sum

print(longestChain(['a', 'b', 'ba', 'bca', 'bda', 'bdca']))



#print(longestChain(['abdcaaaaa']))