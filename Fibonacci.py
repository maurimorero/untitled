def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

def printFibonacci(hows):

    for valor in range(1,hows+1):
        print(fib_recursive(valor))

    return 1

printFibonacci(6)