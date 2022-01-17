from math import ceil, sqrt
def isprime(x):
    if x == 1:
        return False
    if x == 2:
        return True

    upperbound = ceil(sqrt(x))
    for i in range(2,upperbound+1):
        if x % i == 0:
            return False
    
    return True
