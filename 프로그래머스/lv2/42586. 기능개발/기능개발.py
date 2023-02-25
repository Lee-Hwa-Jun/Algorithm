from collections import deque

def solution(progresses,speeds):
    progresses = deque(progresses)
    result = []
    day = 0

    for i,x in enumerate(progresses):
        day_ = int((100-x)/speeds[i]) + 1 if (100-x)/speeds[i] != int((100-x)/speeds[i]) else int((100-x)/speeds[i])
        if day < day_:
            result.append(1)
            day = day_
        else:
            result[-1] += 1
    return result