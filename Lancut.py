# n개의 랜선필요, a가 k개의 랜선 가지고 있음,but k는 값이 제각각임.
#  b는 모두 n개의 같은 길이의 랜선으로 만들고 싶기에 k개의 랜선을 모두 같은 값으로 만들거임.
# 랜선을 자르거나 손실되는 길이는 없음
# 기존의 k개의 랜선으로 n개의 랜선을 만들수 없는 경우는 없음
# cm단위로 정수길이만 자를 것
# 최대 랜선의 길이를 구하는 프로그램 만들 것

#  이분탐색 문제

k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]

start, end = 1, max(a)

while start <= end:
    mid = (start+end)//2
    lines = 0  # 루프마다 초기화 필요
    for x in a:
        lines += x//mid

    if lines >= n:
        start = mid+1
    else:
        end = mid-1

print(end)