
from collections import deque
def solution(people, limit):
    people = sorted(people)
    people = deque(people)
    answer = 0
    if people[0] > limit / 2:
        return len(people)
    if people[-1] <= limit / 2:
        return int(len(people)/2) + int(len(people)%2)
    while len(people) >= 2:
        if people[0]+people[-1] <= limit:
            people.pop()
            people.popleft()
            answer += 1
        else:
            if people[0] > limit/2:
                return answer + len(people)
            people.pop()
            answer += 1
    return answer + len(people)