from collections import Counter
def solution(k,li):
    li = Counter(li)
    li = sorted([li[x] for x in li],reverse=True)
    k_ = 0
    result = 0
    for x in li:
        if k_ < k:
            k_ += x
            result += 1
        else:
            return result
    return len(li)