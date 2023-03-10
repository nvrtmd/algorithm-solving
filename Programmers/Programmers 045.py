# 전화번호 목록
def solution(phone_book):
    phone_dict = {}
    for num in phone_book:
        phone_dict[num] = 0

    for phone_num in phone_book:
        num_string = ''
        for num in phone_num:
            num_string += num
            if num_string != phone_num and num_string in phone_dict:
                return False
    return True

