# 모의고사
def solution(answers):
    answer = []
    scores_list = [0, 0, 0]
    answers_list = ["12345", "21232425", "3311224455"]

    for answer_index in range(len(answers)):
        for i in range(3):
            if answers[answer_index] == int(answers_list[i][answer_index % len(answers_list[i])]):
                scores_list[i] += 1

    for student, score in enumerate(scores_list):
        if score == max(scores_list):
            answer.append(student + 1)

    return answer
