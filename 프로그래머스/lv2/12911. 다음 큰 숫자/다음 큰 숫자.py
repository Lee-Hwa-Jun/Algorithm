def solution(n):
    cnt_n = bin(n).count('1')
    while 1:
        n+=1
        if cnt_n == bin(n).count('1'):
            return n