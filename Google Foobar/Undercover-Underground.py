def choose(n, k):
    """
    Calculates the binomial coefficient for n, k.
    This is equivalent to 'n choose k'.
    """
    key = (n, k)

    if key not in mem_choose:

        if k > n:
            c = 0

        elif k == 0 or n == k:
            c = 1

        elif k == 1 or k == n - 1:
            c = n

        else:
            if k > n / 2:
                k = n - k

            a = 1
            b = 1
            for t in xrange(1, k + 1):
                a *= n
                b *= t
                n -= 1

            c = a // b

        mem_choose[key] = c

    return mem_choose[key]


def possible_graphs(n, k):
    """
    Returns the total number of graphs with that can be formed using
    n nodes and k vertices. This includes graphs that are
    identical for undirected labelled graphs, as well as
    unconnected graphs.
    This function effectively returns the number of ways you can
    choose k vertices out of the 'n choose 2' possible choices.
    """
    if (n, k) not in mem_graphs:
        mem_graphs[(n, k)] = choose(n * (n - 1) >> 1, k)

    return mem_graphs[(n, k)]


def count(n, k):
    """
    Returns the number of distinct, connected, labelled, undirected
    graphs that can be formed using 'n' nodes and 'k' vertices
    """
    if (n, k) in mem_counts:
        # memoized
        return mem_counts[(n, k)]

    if k == n - 1:
        # Cayley's formula
        c = int(n ** (n - 2))

    else:

        # number of possible vertices
        p = n * (n - 1) >> 1

        if k == p:
            # only way is to connect each node to all other nodes,
            # therefore only a single distinct graph
            c = 1

        else:

            # initially all possible graphs
            c = choose(p, k)

            # there can only be duplicates or unconnected components
            # if the number of nodes is less than p - n + 2.
            # equivalent of k < (n - 1 choose 2)
            if k < p - n + 2:

                for i in range(1, n):
                    x = choose(n - 1, i - 1)

                    # minimum of possible vertices for 'i' nodes and 'k'
                    y = min(i * (i - 1) >> 1, k)

                    for j in range(i - 1, y + 1):
                        # exclude invalid graphs from the total
                        c -= x * possible_graphs(n - i, k - j) * count(i, j)

    mem_counts[(n, k)] = c
    return c


def answer(n, k):
    return count(n, k)
