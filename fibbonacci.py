#!/usr/bin/env python
# "Unless you know the code, it has no meaning." ~ John Connolly
__author__ = "hero24"


# Python 2 Memoization example:
def fib(n,mem=[0]):
    # Example of fibonacci sequence with use of memoization
    if n < len(mem):
        return mem[n]
    else:
        if n < 2:
            res = n
            mem += [res]
        else:
            res =  fib(n-1) + fib(n-2)
            mem += [res]
        return res
