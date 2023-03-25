# 순위
def solution(n, results):
    answer = 0
    winners = [set() for _ in range(n + 1)]
    losers = [set() for _ in range(n + 1)]
    for winner, loser in results:
        winners[winner].add(loser)
        losers[loser].add(winner)

    for i in range(1, n + 1):
        for loser in winners[i]:
            losers[loser].update(losers[i])
        for winner in losers[i]:
            winners[winner].update(winners[i])

    for i, j in zip(winners, losers):
        if len(i) + len(j) == n - 1:
            answer += 1
    return answer
