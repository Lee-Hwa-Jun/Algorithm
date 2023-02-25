def solution(n,a,b,cnt = 0):
    if abs(a - b) == 1:
        a_ = int(a / 2) + (1 if a % 2 > 0 else 0)
        b_ = int(b / 2) + (1 if b % 2 > 0 else 0)
        if a_ == b_:
            return cnt + 1
    if a == b:
        return cnt
    a = int(a / 2) + (1 if a % 2 > 0 else 0)
    b = int(b / 2) + (1 if b % 2 > 0 else 0)
    return solution(int(n/2),a,b,cnt+1)