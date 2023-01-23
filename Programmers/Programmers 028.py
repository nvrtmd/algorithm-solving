# 신규 아이디 추천
def solution(new_id):
    new_id = new_id.lower()

    for char in new_id:
        if char in '~!@#$%^&*()=+[{]}:?,<>/':
            new_id = new_id.replace(char, '')

    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    new_id = new_id.strip('.')

    if len(new_id) <= 0:
        new_id = 'a'
    elif len(new_id) >= 16:
        new_id = new_id[:15].strip('.')

    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id

