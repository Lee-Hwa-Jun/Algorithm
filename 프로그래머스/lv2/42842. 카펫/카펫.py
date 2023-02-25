def f(n):
    divisorsList = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ((i ** 2) != n):
                divisorsList.append(n // i)
    return sorted(divisorsList)

def solution(a,b):
    li = f(a+b)
    if len(li)%2 == 0:
        idx_l = int(len(li)/2)-1
        idx_r = int(len(li)/2)
    else:
        idx_l = int(len(li)/2)
        idx_r = int(len(li)/2)
    while 1:
        if (li[idx_l]-2) * (li[idx_r]-2) == b:
            return [li[idx_r],li[idx_l]]
        else:
            idx_l -= 1
            idx_r += 1