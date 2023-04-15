# 단어 변환
from collections import deque


def solution(begin, target, words):
    answer = 0
    words_queue = deque()
    words_queue.append([begin, 0])
    visited = [0 for _ in range(len(words))]

    while words_queue:
        word, count = words_queue.popleft()
        if word == target:
            answer = count
            break

        for i in range(len(words)):
            accord_count = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] == words[i][j]:
                        accord_count += 1

                if accord_count == len(word) - 1:
                    words_queue.append([words[i], count + 1])
                    visited[i] = 1
    return answer
