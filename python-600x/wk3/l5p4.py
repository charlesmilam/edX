def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    gcd = min([a, b])

    while gcd > 0:
        if gcd == 1:
            return gcd
        elif a % gcd == 0 and b % gcd == 0:
            return gcd
        else:
            gcd -= 1
            
