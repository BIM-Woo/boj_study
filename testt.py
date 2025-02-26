#test1
def Skyline(R, C, row_max, col_max): # 2차원 도시 격자 생성
    grid = [[0] * C for _ in range(R)]
    
    for i in range(R): # 각 칸의 높이를 설정 (최소값 사용)
        for j in range(C):
            grid[i][j] = min(row_max[i], col_max[j])  # 최소값을 설정하여 skyline 조건 충족

    for i in range(R): # 검증 1: 행(row)의 최대값이 row_max와 일치하는지 확인
        if max(grid[i]) != row_max[i]:
            return "impossible"

    for j in range(C): # 검증 2: 열(column)의 최대값이 col_max와 일치하는지 확인
        if max(grid[i][j] for i in range(R)) != col_max[j]:
            return "impossible"

    return "possible"

# 🟢 사용자 입력 처리
R, C = map(int, input().split())  # 첫 줄: 행(R)과 열(C) 입력
row_max = list(map(int, input().split()))  # 두 번째 줄: 동쪽 스카이라인 입력
col_max = list(map(int, input().split()))  # 세 번째 줄: 북쪽 스카이라인 입력

# 결과 출력
print(Skyline(R, C, row_max, col_max))

#test2
def skyline_optimized(R, C, row_max, col_max):
    # 🟢 2차원 도시 격자 생성 (캐시 히트 최적화)
    grid = [[0] * C for _ in range(R)]

    # 🟢 행(row) 단위로 먼저 데이터 접근 (최적화된 방식)
    for i in range(R):
        row_max_value = row_max[i]  # 행에서 최댓값 미리 저장 (메모리 접근 최소화)
        for j in range(C):
            grid[i][j] = min(row_max_value, col_max[j])  # 최소값 설정

    # 🟢 검증 1: 행(row) 단위로 검사 (캐시 히트 최적화)
    for i in range(R):
        if max(grid[i]) != row_max[i]:  # 한 번에 한 행씩 접근
            return "impossible"

    # 🟢 검증 2: 열(column) 단위로 검사 (최적화된 방식)
    for j in range(C):
        max_col_value = -1  # 한 번의 스캔으로 최댓값 저장
        for i in range(R):
            if grid[i][j] > max_col_value:
                max_col_value = grid[i][j]
        if max_col_value != col_max[j]:  # 한 번의 스캔으로 비교
            return "impossible"

    return "possible"

# 🟢 사용자 입력 처리
R, C = map(int, input().split())  # 첫 줄: 행(R)과 열(C) 입력
row_max = list(map(int, input().split()))  # 두 번째 줄: 동쪽 스카이라인 입력
col_max = list(map(int, input().split()))  # 세 번째 줄: 북쪽 스카이라인 입력

# 결과 출력
print(skyline_optimized(R, C, row_max, col_max))