from collections import deque
def solution(priorities,location):
    priorities = deque(priorities)
    cnt = 0
    while priorities:
        if max(priorities) == priorities[0]:
            priorities.popleft()
            cnt += 1
            if location == 0: return cnt
            location = location-1 if location > 0 else len(priorities)-1
        else:
            priorities.append(priorities.popleft())
            location = location-1 if location > 0 else len(priorities)-1
    return cnt