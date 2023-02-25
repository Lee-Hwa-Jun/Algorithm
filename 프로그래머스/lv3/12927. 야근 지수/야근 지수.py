from collections import deque
def solution(n,arr):
    if n < 1000 and len(arr) < 5000:
        for x in range(n):
                if max(arr) > 0:
                    arr[arr.index(max(arr))] -= 1
                else:
                    break
    else:
        arr.sort()
        arr = deque(arr)
        temp = [arr.pop(),1]
        while n != 0 and len(arr) > 0:
            if max(temp) == max(arr):
                temp[1] += 1
                arr.pop()
                continue
            elif temp[0] > max(arr):
                if int(n/temp[1])>=1:
                    temp[0] -= 1
                    n -= temp[1]
                else:
                    break
        if int(n/temp[1]) > 0:
            temp[0] -= int(n/temp[1])
            n = n%temp[1]

        for x in range(temp[1]):
            if n > 0:
                arr.append(temp[0]-1 if temp[0]-1 >= 0 else 0)
                n -= 1
            else:
                arr.append(temp[0])
    return sum(map(lambda x : x**2, arr))