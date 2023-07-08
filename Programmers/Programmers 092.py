# [1차] 캐시
from collections import deque


def solution(cacheSize, cities):
    cache = deque()
    time = 0
    cities = [city.upper() for city in cities]
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            time += 5
    return time
