# 카드 뭉치
from collections import deque


def solution(cards1, cards2, goal):
    goal = deque(goal)
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal_length = len(goal)
    for i in range(goal_length):
        if goal[i] in cards1:
            first = cards1.popleft()
            if first != goal[i]:
                return "No"
        elif goal[i] in cards2:
            first = cards2.popleft()
            if first != goal[i]:
                return "No"

    return "Yes"
