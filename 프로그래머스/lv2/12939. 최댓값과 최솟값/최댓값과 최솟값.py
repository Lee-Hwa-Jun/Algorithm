#
def solution(s):
    s = sorted([int(x) for x in s.split()])
    s = list(map(str,s))
    return ' '.join([s[0],s[-1]])