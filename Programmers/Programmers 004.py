# 문자열 압축
def solution(string):
    # 답이 될 수 있는 최대값은 압축이 전혀 되지 않은 string의 길이이므로
    # answer의 초기값을 len(string)으로 설정
    answer = len(string)

    # 한 번에 압축할 수 있는 최소값은 1, 최대값은 string 길이의 절반이므로
    # step(한 번에 압축하는 문자열의 개수)의 범위를 range(1, len(string) // 2 + 1)로 설정
    # step은 1부터 len(string) // 2까지의 숫자가 될 수 있음
    # 즉, 처음엔 1개씩 잘개 쪼개고, 그 다음은 2개씩, 3개씩 늘려가며 쪼개보는 것
    # 마지막엔 문자열을 반으로(=문자열이 데칼코마니처럼 되어 있는 경우) 쪼개서 압축 시도
    for step in range(1, len(string) // 2 + 1):
        # 압축된 문자열을 저장할 변수
        compressed_text = ''
        # step만큼 압축할 것이므로, 가장 처음 비교될 문자열은 처음~step만큼의 범위에 해당
        previous_text = string[:step]
        # count(압축 횟수)는 기본값인 1로 초기화
        count = 1

        # 맨 처음엔 string[:step]과 string[step: step + step + 1]만큼 비교할 것이므로
        # 반복문의 시작값은 step
        # 문자열 전체를 step씩 쪼개어 이전 문자열과 비교해갈 것이므로
        # 반복문의 범위는 range(step, len(string) + step, step)
        for i in range(step, len(string) + step, step):
            # previous_text와 비교할 현재 step 만큼의 text
            current_text = string[i:i + step]

            # 만약 현재 텍스트가 이전 텍스트와 같다면 -> 압축 가능
            # count를 1로 증가시킴
            if current_text == previous_text:
                count += 1

            # 같지 않다면 -> 압축 불가능
            else:
                # previous_text를 compressed_text에 포함시켜야 하므로
                # count가 1보다 크면 count + previous_text,
                # 1보다 작거나 같으면 previous_text만 compressed_text에 이어 붙임
                compressed_text += str(count) + \
                    previous_text if count > 1 else previous_text

                # count를 다시 1로 초기화 후,
                # 현재 텍스트를 그 다음 텍스트에 비교될 previous_text로 설정
                count = 1
                previous_text = current_text

        # step만큼 쪼개서 압축한 경우의 문자열의 길이와
        # 이전 answer(step - 1만큼 쪼개서 압축한 경우의 문자열의 길이)를 비교하여
        # 더 작은 쪽을 answer로 갱신
        answer = min(answer, len(compressed_text))
    return answer
