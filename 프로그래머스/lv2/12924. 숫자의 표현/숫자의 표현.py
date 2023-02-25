def solution(n):
    cnt = 0
    for x in range(1,n+1):
        for y in range(x,n+1):
            s = sum(range(x,y+1))
            if s == n:
                cnt += 1
            if s > n:
                break
    return cnt