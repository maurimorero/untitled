# Complete the mergeArrays function below.
def mergeArrays(a, b):
    c=[]
    for idx in range (len(a)):
        c.append(a[idx])
        c.append(b[idx])
    return (sorted(c))

print (mergeArrays([1,5,7,7],[0,1,2,3]))