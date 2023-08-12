# 할인 행사
def solution(want, number, discount):
    answer = 0
    buy_dict = {}
    bought_dict = {}
    for w, n in zip(want, number):
        buy_dict[w] = n

    for i in range(len(discount) - 10 + 1):
        for product in discount[i: i + 10]:
            if product in buy_dict:
                try:
                    bought_dict[product] += 1
                except:
                    bought_dict[product] = 1

        for key, value in buy_dict.items():
            if key in bought_dict:
                if bought_dict[key] < value:
                    break
                else:
                    continue
            else:
                break
        else:
            answer += 1
        bought_dict = {}
    return answer
