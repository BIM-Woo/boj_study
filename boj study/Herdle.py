# 품종 = 26개 (A - Z) 
# 3x3 격자형태
# 대문자 입력하여 품종 추측하여 유추해야함
# 초록색 강조 = 추측한 품종, 위치 == 일치
# 노란색 강조 = 추측한 품종, 위치 != 일치
# 추측격자= x 정답 격자자 -> y = 초록색 격자 제외 한 노란색 강조 격자

#입력값  처음 3줄 = 정답 격자 3x3 격자
#       다음 3줄 = 추측 격자 3x3 격자
#출력값 처음줄 = 초록색의 개수
#       다음줄 = 노란색의 개수

def count_highlights(answer_grid, guess_grid):
    from collections import Counter

    green_count = 0
    yellow_count = 0

    # 초록색(정확히 일치) 찾기
    answer_positions = {}  # 정답 위치 추적
    guess_positions = {}   # 추측 위치 추적
    answer_counter = Counter()  # 정답 문자 빈도수
    guess_counter = Counter()   # 추측 문자 빈도수

    for i in range(3):
        for j in range(3):
            ans_char = answer_grid[i][j]
            guess_char = guess_grid[i][j]

            if ans_char == guess_char:
                green_count += 1  # 초록색 증가
            else:
                answer_counter[ans_char] += 1
                guess_counter[guess_char] += 1

    # 노란색(위치는 다르지만 존재) 찾기
    for char in guess_counter:
        if char in answer_counter:
            yellow_count += min(answer_counter[char], guess_counter[char])

    return green_count, yellow_count


# 입력 처리
answer_grid = [input().strip() for _ in range(3)]
guess_grid = [input().strip() for _ in range(3)]

# 결과 계산
green, yellow = count_highlights(answer_grid, guess_grid)

# 출력
print(green)
print(yellow)
print(test)