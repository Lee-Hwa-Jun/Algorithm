import re
def solution(file):
    temp = file.copy()
    p1 = re.compile('^\D*')
    p2 = re.compile('\d+')
    temp.sort(key=lambda x: (p1.findall(x)[0].lower(), int(p2.findall(x)[0]), file.index(x)))
    temp = list(map(lambda s:''.join(s),temp))
    return temp