#x,y 주사위 비교 후 높은 숫자가 승리
# x==y 다시 굴림
# x가 y를 이긴다 == x > y 이길 확률

# 4면 주사위 a,b를 기반으로 c 주사위를 구성하여 비이행적 관계를 판별
# C 4면의 숫자는 1 - 10 의 정수

# 입력값 : 첫번째 줄 : T ( 1<= t <= 10) 테스트 케이스의 수
#          다음 T개의 줄 : 각 줄에 8개의 정수 (각 주사위 4면 값) / 앞 4개 : 주사위 A, 뒤 4개 : 주사위 B
# 숫자 정렬되지 않은 상태, 같은 숫자 반복될수 있으니 주의 = combinations_with_replacement

# 출력값 : 각 T개의 줄에 대해 -> 비이행적 관계가 성립하면 "YES" 아니면 "NO"
# 브루트포스 알고리즘 = 모든 경우의 수를 다 해보는 방법(순환관계)

from itertools import combinations_with_replacement

def count_win_probability(d1, d2):
    """ d1이 d2를 이길 확률을 계산 (동점은 무시, 전체 비교 횟수는 16으로 고정) """
    win_count = sum(1 for x in d1 for y in d2 if x > y)  # d1이 이긴 횟수
    return win_count / 16  # 총 16번 비교 (동점 포함)

def is_non_transitive(a, b, c):
    """ A > B, B > C, C > A 가 성립하는지 확인 """
    a_b = count_win_probability(a, b)
    b_c = count_win_probability(b, c)
    c_a = count_win_probability(c, a)
    
    return (a_b > 0.55) and (b_c > 0.55) and (c_a > 0.55)  # 명확한 우위가 있어야 성립

def find_valid_C(a, b):
    """ A와 B를 기반으로 C를 찾아 비이행적 관계를 만족하는지 확인 """
    min_a, max_b = min(a), max(b)
    
    for c in combinations_with_replacement(range(min_a, max_b + 1), 4):  # C의 범위를 최적화
        if is_non_transitive(a, b, c):
            return "yes"
    return "no"

# 입력 처리
t = int(input().strip())  # 테스트 케이스 개수 입력
results = []
for _ in range(t):
    values = list(map(int, input().split()))  # 8개 숫자 입력
    a, b = values[:4], values[4:]  # A, B 분리
    results.append(find_valid_C(a, b))  # 결과 저장

# 최종 결과 출력 (줄바꿈 없이)
print("\n".join(results))

