def suma():
    with open('TestFile.txt') as fp:
        lines = fp.read().split("\n")
    #s="asdasdasdasdS"
    count=0
    for line in lines:
        for i in range(len(line)):
            if (line[i].isupper()):
                count+=1

    return count

print(suma())

