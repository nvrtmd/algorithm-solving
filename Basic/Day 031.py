# BOJ 단계별로 풀어보기
# 2. if문

# 1330
a, b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print("==")


# 9498
grade = int(input())
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")


# 2753
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)


# 14681
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)


# 2884
hour, minute = map(int, input().split())
if minute < 45:
    if hour < 1:
        print(23, 60 - (45-minute))
    else:
        print(hour-1, 60 - (45-minute))
else:
    print(hour, minute - 45)
