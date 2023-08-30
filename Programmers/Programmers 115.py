# Plus Minus
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i < 0:
            negative += 1
        elif i == 0:
            zero += 1
        else:
            positive += 1
    print('{:.6f}'.format(round(positive / len(arr), 6)))
    print('{:.6f}'.format(round(negative / len(arr), 6)))
    print('{:.6f}'.format(round(zero / len(arr), 6)))
