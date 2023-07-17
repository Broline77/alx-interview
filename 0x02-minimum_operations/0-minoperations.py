#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    Returns an integer
    If n is impossible to achieve, returns 0
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    num_chars = 2
    while (num_chars <= n):
        if not (n % num_chars):
            n = int(n / num_chars)
            operations += num_chars
            num_chars = 1
        num_chars += 1
    return operations
