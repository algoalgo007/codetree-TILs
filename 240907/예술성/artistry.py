from collections import deque

ans = 0
n = int(input())
graph = []
graph_cnt = [0] * (n * n + 1)
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
next_graph = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def bfs(x, y, idx):
    cnt = 0
    q = deque()
    q.append((x, y))
    visited[x][y] = idx
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = idx
                q.append((nx, ny))
    return cnt


def score():
    tempScore = 0
    idx = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                idx += 1
                result = bfs(i, j, idx)
                graph_cnt[idx] = result

    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if visited[i][j] != visited[nx][ny]:
                    tempScore += (graph_cnt[visited[i][j]] + graph_cnt[visited[nx][ny]]) * graph[i][j] * graph[nx][ny]
    return tempScore // 2

def turn_cross():
    mx, my = (n-1) // 2, (n-1) // 2
    for i in range(mx + 1, n):
        temp = graph[mx][my + (i-my)]
        graph[mx][my + (i-my)] = graph[i][my]
        graph[i][my] = graph[mx][my - (i - my)]
        graph[mx][my - (i - my)] = graph[mx - (i - mx)][my]
        graph[mx - (i - mx)][my] = temp

def turn_square(sx, sy, square_n):
    for x in range(sx, sx + square_n):
        for y in range(sy, sy + square_n):
            ox, oy = x - sx, y - sy
            rx, ry = oy, square_n - ox -1
            next_graph[rx+sx][ry+sy] = graph[x][y]
    
for _ in range(4):
    ans += score()
    turn_cross()
    square_n = n // 2
    next_graph = [[0] * n for _ in range(n)]
    turn_square(0, 0, square_n)
    turn_square(0, square_n + 1, square_n)
    turn_square(square_n + 1, 0, square_n)
    turn_square(square_n + 1, square_n + 1, square_n)

    for i in range(n):
        for j in range(n):
            if i == n // 2 or j == n // 2:
                continue
            graph[i][j] = next_graph[i][j]

    visited = [[0] * n for _ in range(n)]

print(ans)