#N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올때까지 0의 개수를 세는 문제
#첫째줄 : N (0<=N<=500)
# 츌력 : 0의 개수

import math
import sys

def factorial_count(n):
    product = math.factorial(n)             # N! 계산
    n = str(product)                        # N!을 문자열로 변환
    count = 0                               # 0의 개수 저장 변수 초기화화
    for i in range(len(n)-1, -1, -1):       # 뒤에서부터 거꾸로 탐색 / 인덱스가 0까지 반복하도록 설정 후 반복 방향을 거꾸로 진행행
        if n[i] == '0':                     # 0이면 count 증가
            count += 1                      # 0의 개수 증가
        else:
            break                           # 0이 아닌 수를 만나면 종료
    return count                            # 0의 개수 반환

# 예시 입력
n = int(sys.stdin.readline().strip())  # N 입력
print(factorial_count(n))  # 결과 출력
