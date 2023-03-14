# 2016년
def solution(a, b):
    month_arr = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = b + 5
    day_of_the_week_arr = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    for i in range(a):
        day += month_arr[i]

    return day_of_the_week_arr[day % 7 - 1]
