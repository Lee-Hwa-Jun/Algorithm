from functools import reduce

def solution(data,col,row_begin,row_end):
    data = sorted(data,key = lambda x : (x[col-1],-x[0]))
    temp = []
    for x in range(row_begin-1,row_end):
        temp.append(sum([y%(x+1) for y in data[x]]))
    res = reduce(lambda x, y: x ^ y, temp)
    return res