#의견 X -> 난이도 =0
#의견 1 <= 난이도 = 모든사람의 난이도 의견의 30% 절사평균
#30% 절사평균 = 데이터의 상위 15%. 하위 15% 제외 후 평균 계산
# 제외되는 사람 수는 각각 반올림하여 정수로 계산 = decimal.Decimal(), round()
# 난이도 계산하는 프로그램 작성

#첫번째 줄 = N (0<= n <= 3 * 10^5)
#둘째줄 - 1+n번째줄 제출한 난이도 의견 n개 = 한줄씩 주어짐. (1<= 난이도 의견 <= 30)

import sys
import math

def solved_ac(n, opinions):
    if n == 0:  # 의견이 없는 경우 난이도는 0
        return 0
    
    opinions.sort()  # 의견 정렬

    # 제외할 사람 수 (반올림하여 정수로 계산)
    exclude = math.floor(n * 0.15 + 0.5)  # 0.5를 더한 후 내림 → 올바른 반올림 구현

    # 하위 15%, 상위 15% 제외 (리스트 슬라이싱)
    trimmed_opinions = opinions[exclude:n-exclude]

    # 남은 요소가 없다면 0 반환 (예외 처리)
    if not trimmed_opinions:
        return 0

    # 평균 계산 후 반올림
    return math.floor(sum(trimmed_opinions) / len(trimmed_opinions)+0.5)

# 입력 처리
n = int(sys.stdin.readline().strip())  # 사람 수
opinions = [int(sys.stdin.readline().strip()) for _ in range(n)]  # 난이도 의견

# 결과 출력
print(solved_ac(n, opinions))
