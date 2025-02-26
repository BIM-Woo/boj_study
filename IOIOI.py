# I : N+1개
# O : N개
#I,0 교대로 나오는 문자열  = Pn
#P1 = IOI = 문자열(S), 정수 N이 주어질때때
#P2 = IOIOI
# + OI 추가
#INPUT = 첫째줄 : N / 둘째줄 : M(S의 길이) / 셋째줄 : S
#OUTPUT = S에 Pn이 몇번 나오는지 출력
import sys

def count_pn(n, m, s):
    count = 0  # Pn이 몇 번 등장하는지 카운트
    i = 0  # 문자열 탐색 인덱스
    pattern_count = 0  # 연속된 "OI" 개수
    
      # 투포인터 방법
    while i < m - 1:                # 문자열 끝까지 탐색                      
        if s[i:i+3] == "IOI":  # "IOI" 패턴 찾기
            pattern_count += 1  # "OI" 패턴 개수 증가
            if pattern_count >= n:  # "OI"가 N번 반복되면 Pn 패턴 완성
                count += 1
            i += 2  # "IOI"에서 'I'의 위치로 이동하여 다음 탐색
        else:
            pattern_count = 0  # 연속되지 않으면 초기화
            i += 1  # 다음 문자 탐색

    return count

# 입력 받기
n = int(sys.stdin.readline().strip())  # Pn의 N값
m = int(sys.stdin.readline().strip())  # 문자열 S의 길이
s = sys.stdin.readline().strip()  # 문자열 S

# 결과 출력
print(count_pn(n, m, s))
