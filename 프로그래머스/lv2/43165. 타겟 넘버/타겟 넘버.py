def solution(n,target,dept=0):
    if dept == len(n):
        return 1 if sum(n) == target else 0
    np = n.copy()
    np[dept] = np[dept] * -1
    return solution(n,target,dept+1)+solution(np,target,dept+1)