def solution(cacheSize, cities):
    cache = []
    result = 0
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            result += 1
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)
            result += 5
        cache.append(city)
    return result