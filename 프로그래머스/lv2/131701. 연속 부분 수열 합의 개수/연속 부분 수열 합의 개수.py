from collections import deque
def solution(elements):
    cal = elements+elements
    sumli = deque([])
    for x in range(1,len(elements)+1):
        for y in range(0,len(elements)):
            sumli.append(sum(cal[y:y+x]))
    return len(set(sumli))