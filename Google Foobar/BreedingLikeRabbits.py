cache = {}

def R(n):
    """
    Memoized recursive calculation of R
    """
    if n < 3:
        # base cases
        return [1, 1, 2][n]

    if n not in cache:

        # divide n by two for the factor of 2 "R" formulae
        h = n >> 1

        if n & 1:
            # odd, so follow R(2n+1)
            cache[n] = R(h) + R(h - 1) + 1
        else:
            # even, so follow R(2n)
            cache[n] = R(h) + R(h + 1) + h

    return cache[n]



def search(a, b, target, parity):
    """
    Binary search for target over only odds or evens between a, b
    """
    if b <= a:
        # binary search index overlap - target not found
        return None

    # midpoint
    n = a + ((b - a) >> 1)

    # adjust to correct parity
    n += parity != n & 1

    # calculate R(n) for n
    S = R(n)

    if S == target:
        # these are the numbers you are looking for
        return n

    if S > target:
        # endpoint is now the midpoint
        b = n - 1
    else:
        # starting point is now the midpoint
        a = n + 1

    # keep searching using the adjusted indices
    return search(a, b, target, parity)

def answer(str_S):
    s = int(str_S)

    # search odd first, then even
    return search(0, s, s, 1) or search(0, s, s, 0)
