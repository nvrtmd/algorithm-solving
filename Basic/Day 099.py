# BOJ 단계별로 풀어보기
# 12. 정렬

# 1181
import sys

n = int(sys.stdin.readline())
word_list = []

for i in range(n):
    word_list.append(input())

word_list = list(set(word_list))

word_list.sort()
word_list.sort(key=lambda x: len(x))

for i in word_list:
    print(i)
