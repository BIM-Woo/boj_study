def max_revenue(n, cows):
    cows.sort()  # 학비를 오름차순 정렬
    max_money = 0
    optimal_tuition = 0
    
    for i in range(n):
        tuition = cows[i]  # 현재 학비를 설정
        students = n - i  # 이 학비 이상을 낼 수 있는 학생 수
        revenue = tuition * students  # 총 수익 계산

        if revenue > max_money:  # 더 높은 수익이 나오면 갱신
            max_money = revenue
            optimal_tuition = tuition
        elif revenue == max_money:  # 동일한 수익이면 더 작은 학비 선택
            optimal_tuition = min(optimal_tuition, tuition)

    return max_money, optimal_tuition

# 입력 처리
n = int(input().strip())  # 학생 수
cows = list(map(int, input().strip().split()))  # 각 학생이 낼 수 있는 최대 학비

# 결과 출력
result = max_revenue(n, cows)
print(result[0], result[1])
