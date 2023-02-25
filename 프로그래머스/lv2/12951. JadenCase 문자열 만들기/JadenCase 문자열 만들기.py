
def solution(s):
    active = True
    result = ''
    for x in s:
        if active:
            result += x.upper()
            active = False
        else:
            result += x.lower()
        if x == ' ':
            active = True
    return result