# n개의 정수 A[1], A[2], ..., A[n]이 주어짐
# 이러한 수를 정렬하는 프로그램을 작성
# 첫째 줄에 수의 개수 n(1<=n<=1000)이 주어짐
# 둘째 줄에는 A[1], A[2], ..., A[n]이 주어짐
# 다음 줄에는 m개의 수들이 주어지는데, 이 수들이 A에 포함되어 있는지 알아내면 됨
# 출력값 = m개의 줄에 답을 출력하는데 존재하면 1, 아니면 0을 출력

from collections import Counter

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

counter = Counter(a)
test = []

for x in b:
    if x in counter:
        print(1)
    else:
        print(0)

print(' '.join(map(str, test)))