def solution(n):
    f = [0,1]
    for x in range(2,n+1):
        f.append(f[x-1]+f[x-2])
    return f[-1]%1234567