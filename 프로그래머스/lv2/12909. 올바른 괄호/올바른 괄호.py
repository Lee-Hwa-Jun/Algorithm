from collections import deque

def solution(s):
    que = deque()
    for x in s:
        if x == '(':
            que.append(x)
        elif x == ')':
            if len(que) > 0:
                que.pop()
            else:
                return False
    if que:
        return False
    return True