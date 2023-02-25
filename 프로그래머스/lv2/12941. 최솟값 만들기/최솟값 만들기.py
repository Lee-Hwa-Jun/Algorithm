def solution(A,B):
    A.sort()
    B.sort()
    B.reverse()
    s = 0
    for x in range(len(A)):
        s += A[x]*B[x]
    return s