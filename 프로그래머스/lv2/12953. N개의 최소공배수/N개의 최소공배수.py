def lcm(a,b):
    for x in range(max(a,b),(a*b)+1):
        if x%a == 0 and x%b == 0:
            return x

def solution(arr):
    result = 0
    for x in arr:
        if result == 0:
            result = x
        else:
            result = lcm(result,x)
    return result