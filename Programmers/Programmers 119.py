import sys

read = sys.stdin.readline
brackets = read().strip()

brackets_dict = {'small': {'(': 0, ')': 0, }, 'medium': {
    '[': 0,  ']': 0}, 'large': {'{': 0, '}': 0}}

brackets_stack = []
for b in brackets:
    if b in '()':
        brackets_dict['small'][b] += 1
    elif b in '[]':
        brackets_dict['medium'][b] += 1
    else:
        brackets_dict['large'][b] += 1


for each_bracket_dict in brackets_dict.values():
    if len(set(each_bracket_dict.values())) > 1:
        print(False)
        break
else:
    print(True)
