#!usr/bin/python3

def minoperations(n):
    """
    This function calculates the fewest number 
    of operations needed to result in exactly n H characters in the file.
    """
    
    if (n <= 0):
        return 0

    # Init result
    ops = 0

    # Divide by 2 if n is even
    if (n % 2 == 0):
        ops += minoperations(n // 2)
        ops += 1

    else:
        ops += minoperations(n - 1)
        ops += 1

    return ops