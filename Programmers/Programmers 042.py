# 튜플
def solution(s):
    answer = []
    string = s[1: len(s) - 1]
    num = ''
    nums_arr = []
    nums_arr_dict = {}
    nums_store_mode = False

    for str in string:
        if str == '{':
            nums_store_mode = True
            continue
        if nums_store_mode:
            if str.isdigit():
                num += str
            else:
                nums_arr.append(int(num))
                num = ''
                if str == '}':
                    nums_store_mode = False
                    nums_arr_dict[len(nums_arr)] = nums_arr
                    nums_arr = []

    nums_arr_dict = sorted(nums_arr_dict.items())

    for sorted_nums_arr in nums_arr_dict:
        for num in sorted_nums_arr[1]:
            if num not in answer:
                answer.append(num)

    return answer
