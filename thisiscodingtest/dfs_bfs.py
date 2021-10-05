from collections import deque

# 팩토리얼 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# 유클리드 호제법 (최대공약수 계산)
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))

# DFS 정의
def dfs(graph, v, visited):
    visited[v] = True  # 현재 노드 방문 처리
    print(v, end=" ")
    for i in graph[v]:  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 정의
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True  # 현재 노드를 방문 처리
    while queue:  # 큐가 빌 때까지 반복
        v = queue.popleft()  # 큐에서 하나의 원소를 뽑아 출력
        print(v, end=" ")
        for i in graph[v]:  # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

dfs(graph, 1, visited)
bfs(graph, 1, visited)
