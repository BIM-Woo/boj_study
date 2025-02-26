#총 Sa+1,Sa+2,...,Sn-b-1,Sn-b 번 과일

#문제
#과일 2종류 이하 사용 + 가장 많은 과일 개수를를 출력

#과일 종류 : S1, S2, S3, S4, S5, S6, S7, S8, S9 (2개 이하로 선택택)
# 과일 개수 : N (1<=N<=200000)
#총 n-(a+b)개의 과일 (0<=a,b /  a+b<N)
#앞에서 a개, 뒤에서 b개 빼서 2개 이하로 선택



from collections import Counter  # Counter 함수 사용
import sys                       # sys 모듈 사용

def max_fruit_count(n, fruits):  #투 포인터 알고리즘으로 변수 초기화
    left = 0                     # 왼쪽 포인터
    max_count = 0                # 최대 과일 개수
    fruit_count = Counter()      # 과일 개수를 세는 딕셔너리
 
    for right in range(n):                          # 오른쪽 포인터 이동     
        fruit_count[fruits[right]] += 1             # 과일 개수 세기

        while len(fruit_count) > 2:                 # 과일 종류가 2개 초과일 경우 left로 이동
            fruit_count[fruits[left]] -= 1          # left위치 과일 개수 줄이기기
            if fruit_count[fruits[left]] == 0:      # 과일 개수가 0이면 삭제
                del fruit_count[fruits[left]]       
            left += 1                               # 0일 경우 제거 후 한칸 이동해서 다음 과일 검사 반복

        max_count = max(max_count, sum(fruit_count.values())) # 최대 과일 개수 갱신

    return max_count                                # 최대 과일 개수 반환

n = int(sys.stdin.readline().strip())                                # 과일 개수
fruits = list(map(int, sys.stdin.readline().strip().split()))        # 과일 종류

print(max_fruit_count(n, fruits))                                    # 최대 과일 개수 출력
