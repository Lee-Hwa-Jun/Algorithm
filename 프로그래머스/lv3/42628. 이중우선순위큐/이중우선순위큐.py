from collections import deque
def solution(arr):
    que = deque([])
    for k in arr:
        k = k.split()
        if k[0] == 'I':
            que.append(int(k[1]))
        elif que and k[0] == 'D' and k[1] == '-1':
            que.remove(min(que))
        elif que and k[0] == 'D' and k[1] == '1':
            que.remove(max(que))
    return [max(que),min(que)] if que else [0,0]