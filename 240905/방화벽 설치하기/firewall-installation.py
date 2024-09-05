from itertools import combinations
import copy
from collections import deque

n, m = map(int, input().split())

graph = []
blank = []
fire = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
visited = [[False] * m for _ in range(n)]

def bfs():
    copyGraph = copy.deepcopy(graph)
    q = deque()
    for i in range(len(fire)):
        x = fire[i][0]
        y = fire[i][1]
        q.append((x, y))
    visited[fire[0][0]][fire[0][1]] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if copyGraph[nx][ny] == 0 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
                copyGraph[nx][ny] = 2
    cnt = 0 
    for i in range(n):
        for j in range(m):
            if copyGraph[i][j] == 0:
                cnt += 1
    return cnt

for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append((i, j))
        elif graph[i][j] == 2:
            fire.append((i, j))

for c in combinations(blank, 3):
    for x, y in list(c):
        graph[x][y] = 1
    visited = [[False] * m for _ in range(n)] 
    result = bfs()
    answer = max(answer, result)
    for x, y in list(c):
        graph[x][y] = 0
print(answer)