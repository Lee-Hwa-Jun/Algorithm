from collections import deque
def solution(s):
    dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    s = deque([x for x in s])
    stack = deque([])
    result = deque([])
    stack.append(s.popleft())
    while s:
        if ''.join(stack) in dic.keys() and s:
            stack.append(s.popleft())
        else:
            if len(stack) > 1:
                t = stack.pop()
                result.append(dic[''.join(stack)])
                dic[''.join(stack)+t] = max(dic.values()) + 1
                stack = deque([t])
            else:
                dic[''.join(stack)] = max(dic.values())+1
                result.append(dic[''.join(stack)])
    if len(stack) > 0:
        if ''.join(stack) in dic.keys():
            result.append(dic[''.join(stack)])
        else:
            dic.setdefault(''.join(stack),max(dic.values()) + 1)
            t = stack.pop()
            if ''.join(stack) in dic.keys():
                result.append(dic[''.join(stack)])
                result.append(dic[t])
            else:
                result.append(dic[''.join(stack)+t])

    return list(result)