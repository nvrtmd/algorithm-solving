# BOJ 단계별로 풀어보기
# 1. 입출력과 사칙연산

# 10171
cat = ["\    /\\", " )  ( ')", "(  /  )",  " \(__)|"]
for i in range(len(cat)):
    print(cat[i])


# 10172
dog = ['|\_/|', '|q p|   /}', '( 0 )"""\\',  '|"^"`    |', '||_/=\\\\__|']
for i in range(len(dog)):
    print(dog[i])


# 1000, 1001, 10998, 1008
a, b = map(int, input().split())
print(a+b)

print(a-b)

print(a*b)

print(a // b)

print(a % b)


# 10869, 10430
a, b, c = map(int, input().split())
print((a+b) % c)
print(((a % c) + (b % c)) % c)
print((a*b) % c)
print(((a % c) * (b % c)) % c)
print(a % b)


# 2588
a = int(input())
b = input()
list_b = list(b)
for i in range(3):
    print(a * int(list_b[3-i-1]))
print(a * int(b))
