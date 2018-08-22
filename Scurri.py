#Write a program that prints the numbers from 1 to 100. But for multiples of three print “Three” instead of the number
# and for the multiples of five print “Five”. For numbers which are multiples of both three and five print “ThreeFive”.

def solution():

    for value in range (1,101):
        if (value%3==0) and (value%5==0):
            print ("ThreeFive")
        elif (value%3==0):
            print ("Three")
        elif (value % 5 == 0):
            print("Five")
        else:
            print(value)

solution()