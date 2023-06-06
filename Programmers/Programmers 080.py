# 주차 요금 계산
import math


def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees

    dic = {}
    for i in records:
        time, car_num, _ = i.split(' ')
        try:
            dic[car_num]
        except:
            dic[car_num] = []
        finally:
            hour, minute = time.split(':')
            time = int(hour) * 60 + int(minute)
            dic[car_num].append(time)

    answer_dic = {car_num: 0 for car_num in sorted(dic.keys())}

    for car_num, park_time in dic.items():
        total_time = 0
        if len(park_time) % 2 != 0:
            park_time.append(1439)

        for i in range(0, len(park_time) - 1, 2):
            total_time += park_time[i+1] - park_time[i]

        if total_time > basic_time:
            left_time = total_time - basic_time
            answer_dic[car_num] = basic_fee + \
                math.ceil(left_time / unit_time) * unit_fee
        else:
            answer_dic[car_num] = basic_fee

    return list(answer_dic.values())

