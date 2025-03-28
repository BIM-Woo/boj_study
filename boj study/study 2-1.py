import time

# 🟢 데코레이터: 함수 실행 시간을 측정하는 함수
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 시작 시간 기록
        result = func(*args, **kwargs)  # 원래 함수 실행
        end_time = time.time()  # 종료 시간 기록
        print(f"{func.__name__} 실행 시간: {end_time - start_time:.6f} 초")  # 실행 시간 출력
        return result
    return wrapper

# 🟢 최적화된 Skyline 검사 (리스트 사용 최소화 + 한 번의 루프로 검증)
@timeit
def skyline_fastest(R, C, row_max, col_max):
    # ✅ 각 행(row)과 열(column)의 최대값을 직접 비교 (grid 리스트 생성 X)
    
    # 열(column)에서의 최대값을 저장하는 배열
    max_col_values = [0] * C  

    # 1️⃣ 행(row) 단위로 스캔하면서 동시에 열(column) 최대값을 계산
    for i in range(R):
        row_max_value = row_max[i]  # 해당 행에서의 최대값
        
        for j in range(C):
            height = min(row_max_value, col_max[j])  # 실제 건물 높이 결정
            max_col_values[j] = max(max_col_values[j], height)  # 열의 최대값 갱신

        # 🚀 행의 최대값이 `row_max[i]`와 일치하는지 즉시 확인
        if max_col_values[j] != row_max_value:
            return "impossible"

    # 2️⃣ 열(column) 단위로 검증 수행
    for j in range(C):
        if max_col_values[j] != col_max[j]:  # 🚀 각 열의 최대값이 `col_max[j]`와 같은지 확인
            return "impossible"

    return "possible"

# 🟢 사용자 입력 처리
R, C = map(int, input().split())  # 첫 줄: 행(R)과 열(C) 입력
row_max = list(map(int, input().split()))  # 두 번째 줄: 동쪽 스카이라인 입력
col_max = list(map(int, input().split()))  # 세 번째 줄: 북쪽 스카이라인 입력

# 🟢 실행 시간 비교
print(skyline_fastest(R, C, row_max, col_max))
