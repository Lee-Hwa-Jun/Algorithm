def solution(fees,record):
    dic = {}
    result = []
    for x in record:
        car = x.split(' ')
        dic.setdefault(car[1],[])
        time = list(map(int,car[0].split(':')))
        time = time[0] * 60 + time[1]
        if len(dic[car[1]])%2 == 1 and car[2] == 'IN':
            dic[car[1]].append(1439)
        dic[car[1]].append(time)
    for x in sorted(dic.keys()):
        if len(dic[x])%2 != 0:
            dic[x].append(1439)
        money = fees[1]
        nt = 0
        for k in range(0,len(dic[x]),2):
            nt += dic[x][k+1] - dic[x][k]
        nt = nt-fees[0]
        k,v = divmod(nt if nt > 0 else 0,fees[2])
        money += fees[3]*k
        money += fees[3] if v > 0 else 0
        result.append(money)

    return result