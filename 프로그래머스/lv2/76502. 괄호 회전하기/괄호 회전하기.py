from collections import deque

def isright(sli):
    dic = {'[':']','{':'}','(':')'}
    stack = deque([])
    for x in sli:
        if x in dic.keys():
            stack.append(x)
        if x in dic.values():
            if stack:
                if dic[stack[-1]] == x:
                    stack.pop()
            else:
                return 0
    if stack:
        return 0
    else:
        return 1

def solution(s):
    s = deque([x for x in s])
    cnt = 0
    for x in range(len(s)):
        s.append(s.popleft())
        cnt += isright(s)
    return cnt