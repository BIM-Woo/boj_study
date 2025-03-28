#플로이드 와샬 알고리즘 : 모든 정점에서 모든 정점으로의 최단 경로를 구하는 알고리즘
#케빈 베이컨 수 : 모든 사람과 케빈 베이컨 게임을 했을 때, 케빈 베이컨 게임의 단계의 총 합

#  유저 수 : (2<=n<=100)
#  친구 관계 수 : 1<= m <= 5000
# 둘째 줄부터 M개의 줄에는 친구관계가 주어짐
# A,B 로 이루어져 있음 / A,B가 친구 = B,A도 친구 / A=!B / 중복되어 돌아올 수 있음 / 친구가 1명도 없는 사람은 없음 / 모든 사람들은 친구로 연결되어 있음
# 사람 번호 : 1~N (같은 번호 X )
# 케빈 베이컨 수가 가장 작은 사람 출력( 여러명일 경우 번호가 가장 작은 사람 출력)

import sys

def floyd_warshall(n, dist):                                             # 플로이드-와샬 알고리즘 실행
    for k in range(1, n + 1):                                            # 거쳐가는 노드
        for i in range(1, n + 1):                                        # 출발 노드
            for j in range(1, n + 1):                                    # 도착 노드
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

def find_min_kevin_bacon(n, dist):
    min_bacon = float('inf')
    min_person = -1

    for i in range(1, n + 1):
        bacon_sum = sum(dist[i][1:])  # i번 사람의 케빈 베이컨 수 계산
        if bacon_sum < min_bacon:
            min_bacon = bacon_sum
            min_person = i  # 최소 케빈 베이컨 수를 가진 사람 저장

    return min_person

# 입력 받기
n, m = map(int, sys.stdin.readline().split())  # 사람 수, 친구 관계 수
INF = float('inf')
dist = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신은 거리 0으로 설정
for i in range(1, n + 1):
    dist[i][i] = 0

# 친구 관계 입력받아 거리 1로 설정
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dist[a][b] = 1
    dist[b][a] = 1  # 양방향 그래프

# 플로이드-와샬 알고리즘 수행
floyd_warshall(n, dist)

# 케빈 베이컨 수가 가장 작은 사람 찾기
result = find_min_kevin_bacon(n, dist)
print(result)
