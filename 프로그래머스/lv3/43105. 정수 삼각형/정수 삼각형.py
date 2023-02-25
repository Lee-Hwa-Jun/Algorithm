def solution(arr):
    for k in range(len(arr)-1,-1,-1):
        for x in range(0,len(arr[k])-1):
            arr[k-1][x] = arr[k-1][x] + max(arr[k][x],arr[k][x+1])
    return arr[0][0]