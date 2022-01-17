def isprime(x):
    from math import sqrt, ceil
    if x == 1:
        return False
    if x == 2:
        return True

    for i in range(2, ceil(sqrt(x)+1)):
        if x % i == 0:
            return False

    return True
