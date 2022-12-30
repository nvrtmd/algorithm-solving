# 버스 여행
def solution(n, signs):
    for start in range(n):
        next_stops = [index for index, stop in enumerate(
            signs[start]) if stop]
        print('next_stops', next_stops)
        while next_stops:
            next_stop = next_stops.pop()
            print('next_stop', next_stop)
            print('signs[next_stop]', signs[next_stop])
            for end, pos in enumerate(signs[next_stop]):
                print('end', end, 'pos', pos)
                if pos and signs[start][end] == 0:
                    print('start', start, 'end', end)
                    signs[start][end] = 1
                    next_stops.append(end)
    return signs
