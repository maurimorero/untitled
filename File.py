
file1 = open("TestFile.txt","w")

file1.write("Hello World \n")
file1.write("This is our new text file")
file1.write("and this is another line.")
file1.write("Why? Becausewe can.")

file1.close()

with open('TestFile.txt') as fp:
    lines = fp.read().split("\n")

print (lines)



