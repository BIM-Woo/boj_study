# d1 = b1 건초 아침에 도착 후 저녁부터 식사가능
# 문제 : T일 동안 소가 먹을수 있는 건초의 총량

# 입력값 : 첫번째 줄 : n(건조 도착하는 날짜 개수),t(계산할 일수) / 두번재 줄 : d1 = (건조가 도착하는 날짜), b1 = (건초의 개수) 

import sys

def count_haybales_eaten(N, T, deliveries):
    haybales = 0  # 현재 창고에 있는 건초 개수
    eaten = 0  # Bessie가 먹은 총 건초 개수
    day = 1  # 현재 날짜 (1일부터 시작)

    for d, b in deliveries:
        # d일까지 가능한 만큼 소비
        days_to_eat = min(d - day, haybales)  # 현재 haybales로 버틸 수 있는 날짜
        eaten += days_to_eat
        haybales -= days_to_eat
        day += days_to_eat  # 다음으로 이동할 날짜 갱신

        if day > T:
            break  # 목표 날짜를 초과하면 종료

        # 새로운 건초를 창고에 추가
        haybales += b

    # 남아 있는 건초를 추가 소비할 수 있음
    eaten += min(T - day + 1, haybales)

    return eaten

# 입력 처리
def main():
    input = sys.stdin.read
    data = input().splitlines()

    N, T = map(int, data[0].split())
    deliveries = [tuple(map(int, line.split())) for line in data[1:N + 1]]

    # 결과 출력
    print(count_haybales_eaten(N, T, deliveries))

if __name__ == "__main__":
    main()

