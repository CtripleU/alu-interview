def minoperations(n):
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