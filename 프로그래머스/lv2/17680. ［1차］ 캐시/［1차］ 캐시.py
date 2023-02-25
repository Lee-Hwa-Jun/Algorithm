def solution(cachesize,cities):
    cache = []
    time = 0
    for city in cities:
        if cachesize:
            if city.lower() in cache:
                cache.remove(city.lower())
                cache.append(city.lower())
                time+=1
            else:
                if len(cache) >= cachesize:
                    cache.pop(0)
                cache.append(city.lower())
                time+=5
        else:
            time+=5
    return time