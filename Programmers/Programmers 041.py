# 뉴스 클러스터링
import math


def make_multi_set(string):
    arr = []
    for i in range(len(string) - 1):
        if string[i:i + 2].isalpha():
            arr.append(string[i:i + 2].upper())
    return arr


def solution(str1, str2):
    str1_multi_set = make_multi_set(str1)
    str2_multi_set = make_multi_set(str2)
    if str1_multi_set == [] and str2_multi_set == []:
        return 65536
    inter_arr = []
    union_arr = []
    str1_multi_set_copy = str1_multi_set.copy()
    str2_multi_set_copy = str2_multi_set.copy()

    for i in str1_multi_set:
        if i in str2_multi_set_copy:
            inter_arr.append(i)
            str1_multi_set_copy.remove(i)
            str2_multi_set_copy.remove(i)
    union_arr = inter_arr + str1_multi_set_copy + str2_multi_set_copy
    return math.floor((len(inter_arr) / len(union_arr)) * 65536)
