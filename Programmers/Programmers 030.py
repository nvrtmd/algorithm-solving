# [카카오 인턴] 키패드 누르기
def solution(numbers, hand):
    answer = ''
    right_hand = '#'
    left_hand = '*'
    right_numbers = [3, 6, 9]
    left_numbers = [1, 4, 7]

    key_pads = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                4: [1, 0], 5: [1, 1], 6: [1, 2],
                7: [2, 0], 8: [2, 1], 9: [2, 2],
                '*': [3, 0], 0: [3, 1], '#': [3, 2]}

    for number in numbers:
        if number in right_numbers:
            right_hand = number
            answer += 'R'
        elif number in left_numbers:
            left_hand = number
            answer += 'L'
        else:
            right_hand_position = key_pads[right_hand]
            left_hand_position = key_pads[left_hand]
            number_position = key_pads[number]
            right_distance = 0
            left_distance = 0
            for i in range(2):
                right_distance += abs(
                    number_position[i] - right_hand_position[i])
                left_distance += abs(number_position[i] -
                                     left_hand_position[i])

            if right_distance > left_distance:
                left_hand = number
                answer += 'L'
            elif right_distance < left_distance:
                right_hand = number
                answer += 'R'
            else:
                if hand == 'right':
                    right_hand = number
                else:
                    left_hand = number
                answer += hand[0].upper()
    return answer
