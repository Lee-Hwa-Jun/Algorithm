from collections import deque
def solution(s):
    que = deque([])
    for x in s:
        que.append(x)
        while 1:
            if len(que) >=2 and que[-1] == que[-2]:
                que.pop()
                que.pop()
            else: break
    return 0 if que else 1