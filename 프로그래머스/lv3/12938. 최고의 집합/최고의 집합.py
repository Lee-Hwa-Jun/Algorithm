def solution(n,s):
    if s // n <= 0: return [-1]
    k,v = divmod(s,n)
    temp = []
    for x in range(n):
        if v > 0:
            temp.append(k+1)
            v -= 1
        else:
            temp.append(k)
    return sorted(temp)