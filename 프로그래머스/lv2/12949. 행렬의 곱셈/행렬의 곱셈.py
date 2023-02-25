def sum_(a1,a2):
    s = 0
    for x in range(len(a1)):
        s += a1[x]*a2[x]
    return s

def solution(arr1,arr2):
    result = []
    arr2 = list(zip(*arr2))
    for i in range(len(arr1)):
        temp = []
        for x in arr2:
            temp.append(sum_(arr1[i],x))
        result.append(temp)
    return result