# N으로 표현
def solution(N, number):
    arr = [None] + [{int(str(N)*i)} for i in range(1, 9)]
    print(arr)
    for i in range(1, 9):
        print('I', i)
        for j in range(1, i):
            print('J', j)
            for num1 in arr[j]:
                print('num1', num1)
                for num2 in arr[i-j]:
                    print('num2', num2)
                    arr[i].add(num1 + num2)
                    arr[i].add(num1 - num2)
                    arr[i].add(num1 * num2)
                    if num2:
                        arr[i].add(num1 // num2)
                    print('arr', arr)

        if number in arr[i]:
            return i

    return -1
