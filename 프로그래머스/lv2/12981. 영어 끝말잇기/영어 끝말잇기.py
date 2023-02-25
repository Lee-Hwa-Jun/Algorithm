from collections import deque
def solution(n,words):
    words = deque(words)
    passed = deque([])
    word = words.popleft()
    passed.append(word)
    person = 1
    turn = 1
    isok = True
    while words:
        person += 1
        if person > n:
            turn += 1
            person = 1
        if word[-1] != words[0][0] or words[0] in passed:
            isok = False
            passed.append(words.popleft())
            break
        if word[-1] == words[0][0]:
            word = words.popleft()
            passed.append(word)
    if isok:
        return [0,0]
    else:
        return [person,turn]