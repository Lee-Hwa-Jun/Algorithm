def solution(s):
    result = []
    s = s.replace('{','[').replace('}',']')
    s = eval(s)
    s.sort(key=len)
    for x in s:
        result.append(list(set(x).symmetric_difference(result))[0])
    return result