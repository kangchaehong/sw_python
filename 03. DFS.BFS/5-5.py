# n! = 1*2*3*...*(n-1)*n

def factorial(n) :
    if n <= 1 :
        return 1
    return n * factorial(n-1)