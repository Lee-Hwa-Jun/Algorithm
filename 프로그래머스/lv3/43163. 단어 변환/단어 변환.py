def diff(begin,target):
    cnt = 0
    begin = [s for s in begin]
    target = [s for s in target]
    while begin:
        if begin.pop() != target.pop():
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def solution(begin,target,words):
    if target not in words:
        return 0
    words.remove(target)
    if len(words) == 1 and diff(begin,target):
        return 1
    if diff(begin,target):
        return 1
    temp = [1+solution(begin,x,words) if diff(target,x) else 0 for x in words]
    return min(filter(lambda x:x>0,temp))