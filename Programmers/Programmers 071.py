# 영어 끝말잇기
def solution(n, words):
    answer = []
    said_words = []

    for i, word in enumerate(words):
        if len(said_words) and (word in said_words or word[0] != said_words[-1][-1]):
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break
        else:
            said_words.append(word)

    return answer if len(answer) else [0, 0]
