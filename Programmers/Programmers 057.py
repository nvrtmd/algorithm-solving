# 불량 사용자
from itertools import permutations


def checkUsers(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            elif users[i][j] != banned_id[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    users_permutations = list(permutations(user_id, len(banned_id)))

    for users in users_permutations:
        if checkUsers(users, banned_id):
            users = set(users)
            if users not in answer:
                answer.append(users)
        else:
            continue

    return len(answer)
