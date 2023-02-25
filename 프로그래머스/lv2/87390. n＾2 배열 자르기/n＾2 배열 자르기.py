def solution(n,left,right):
    result = []
    for x in range(left,right+1):
        k,v = divmod(x,n)
        result.append(v+1 if v>k else k+1)
    return result