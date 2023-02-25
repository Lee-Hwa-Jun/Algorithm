def solution(b,s=0,c=0):
    c += 1
    temp_1 = b.count('1')
    temp_0 = b.count('0')
    s += temp_0
    if b.replace('0','') == '1':
        return [c,s]
    else:
        return solution(bin(temp_1)[2:],s,c)