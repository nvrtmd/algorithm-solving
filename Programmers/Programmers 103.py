# 주식가격
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for time, price in enumerate(prices):
        if len(stack) == 0:
            stack.append([time, price])
            continue

        while stack:
            last_time, last_price = stack.pop()
            if last_price > price:
                answer[last_time] = time - last_time
            else:
                stack.append([last_time, last_price])
                break
        stack.append([time, price])

    for stock in stack:
        time, price = stock
        answer[time] = len(prices) - 1 - time
    return answer
