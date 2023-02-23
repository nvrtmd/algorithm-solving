# 멀쩡한 사각형
def solution(w, h):
    answer = 0
    if w == h:
        return w * h - w
    elif w == 1 or h == 1:
        return 0
    for i in range(1, w + 1):
        answer += h * (w - i) // w
    return answer * 2
