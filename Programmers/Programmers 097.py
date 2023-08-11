# [3차] 압축
def solution(msg):
    answer = []
    alphabet_ord = [i for i in range(65, 91)]
    alphabet_dict = {chr(alphabet): i + 1 for i,
                     alphabet in enumerate(alphabet_ord)}
    idx = 0
    while True:
        start_word = msg[idx]
        full_word = start_word
        pointer = 1
        for next_word in msg[idx + 1:]:
            full_word += next_word
            if full_word in alphabet_dict:
                pointer += 1
            else:
                alphabet_dict[full_word] = len(alphabet_dict) + 1
                curr_word = full_word[:len(full_word) - 1]
                answer.append(alphabet_dict[curr_word])
                idx += pointer
                break
        else:
            answer.append(alphabet_dict[full_word])
            break

    return answer
