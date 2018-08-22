# Complete the longestChain function below.
def longestChain(words):
    counts=[]

    for word in words:
        if len(word)==1:
            counts.append(0)
            continue
        sum=0
        leng=len(word)
        subword=word[:-1]
        #print(subword)
        while(leng>1):
            print(subword)
            if(words.count(subword)>0):
                sum+=1
                subword = subword[:-1]
                leng -= 1
            else:
                leng=0

        counts.append(sum)
    print(counts)
    return max(counts)

print (longestChain(['a','b','ba','bca','bda','bdca']))
