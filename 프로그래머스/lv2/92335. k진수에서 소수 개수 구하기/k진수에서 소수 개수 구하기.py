
from collections import Counter
def is_prime_number(num):
    if num == 1: return 0
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return 0
        return 1

def nd(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    rev_base = rev_base[::-1].split('0')
    rev_base = list(map(int,filter(lambda x: len(x)>0,rev_base)))

    return rev_base

def solution(n,k):
    n = Counter(nd(n,k))
    return sum(map(lambda x : n[x] if is_prime_number(x) else 0,n.keys()))
