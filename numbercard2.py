# 카드는 정수값 = m개(중복 x), 갯수는 n 개(중복 가능) , 중복이 있다면 n값이 더 큼
# 
# 첫째줄 m , 둘째줄 숫자 카드의 정수 값을 공백으로 나누어서 입력값  
# 몇개의 카드를 가지고 있는지 공백으로 구분한 n 개의 총 카드의 종류 갯수 출력
from collections import Counter

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

counter = Counter(a)
test = []

for x in b:
    test.append(counter[x])

print(' '.join(map(str, test)))