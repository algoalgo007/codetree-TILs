from collections import deque

r, c, k = map(int, input().split())
graph = [[0] * c for _ in range(r + 3)]
exit = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
path = []

def turn_cw(dir):
    if dir == 3:
        return 0
    else:
        return dir + 1

def turn_ccw(dir):
    if dir == 0:
        return 3
    else:
        return dir - 1

def find_exit(exit, x, y, dir):
    ex = x + dx[dir]
    ey = y + dy[dir]
    exit.append((ex, ey))

def inbound(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
    if x1 < 3 or y1 < 0 or x1 >= r + 3 or y1 >= c:
        return False
    if x2 < 3 or y2 < 0 or x2 >= r + 3 or y2 >= c:
        return False
    if x3 < 3 or y3 < 0 or x3 >= r + 3 or y3 >= c:
        return False
    if x4 < 3 or y4 < 0 or x4 >= r + 3 or y4 >= c:
        return False
    if x5 < 3 or y5 < 0 or x5 >= r + 3 or y5 >= c:
        return False
    return True

def bfs(graph, visited, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        path.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r + 3 or ny >= c:
                continue
            if graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
            if (x, y) in exit and graph[nx][ny] != 0 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True

idx = 0
for _ in range(k):
    idx += 1
    ci, di = map(int, input().split())
    ci -= 1
    x1, y1 = 1, ci - 1
    x2, y2 = 2, ci
    x3, y3 = 1, ci + 1
    x4, y4 = 1, ci
    x5, y5 = 0, ci
    while True:
        tx1 = x1; ty1 = y1
        tx2 = x2; ty2 = y2
        tx3 = x3; ty3 = y3
        tx4 = x4; ty4 = y4
        tx5 = x5; ty5 = y5
        if tx2 + 1 >= r + 3: # 아래로 이동하니 그래프 나가는 경우
            break
        if graph[tx1+1][ty1] == 0 and graph[tx2+1][ty2] == 0 and graph[tx3+1][ty3] == 0: # 아래로 이동 가능
            x1 = x1 + 1; y1 = y1
            x2 = x2 + 1; y2 = y2
            x3 = x3 + 1; y3 = y3
            x4 = x4 + 1; y4 = y4
            x5 = x5 + 1; y5 = y5
            continue
        if ty1 - 1 >= 0: # 좌측 이동해도 그래프 안 나가는 경우
            if (graph[tx1][ty1-1] == 0 and graph[tx2][ty2-1] == 0 and graph[tx5][ty5-1] == 0
                    and graph[tx1+1][ty1-1]==0 and graph[tx2+1][ty2-1] == 0): # 좌측 아래 이동 가능한 경우
                x1 = x1 + 1; y1 = y1 - 1
                x2 = x2 + 1; y2 = y2 - 1
                x3 = x3 + 1; y3 = y3 - 1
                x4 = x4 + 1; y4 = y4 - 1
                x5 = x5 + 1; y5 = y5 - 1
                di = turn_ccw(di)
                continue
            else: # 좌측 아래 이동 불가능 우측 아래로 이동
                if ty3 + 1 <= c-1:
                    if (graph[tx2][ty2+1] == 0 and graph[tx3][ty3+1] == 0 and graph[tx5][ty5+1] == 0
                            and graph[tx3+1][ty3+1] == 0 and graph[tx2+1][ty2+1] == 0):
                        x1 = x1 + 1; y1 = y1 + 1
                        x2 = x2 + 1; y2 = y2 + 1
                        x3 = x3 + 1; y3 = y3 + 1
                        x4 = x4 + 1; y4 = y4 + 1
                        x5 = x5 + 1; y5 = y5 + 1
                        di = turn_cw(di)
                        continue
                    else: # 좌하단 우하단 둘다 이동 불가능 한 경우
                        break
                else:
                    break
        else: # 좌측 이동하면 그래프 나가는 경우 우측으로 접근
            if ty3 + 1 <= c - 1:
                if (graph[tx2][ty2 + 1] == 0 and graph[tx3][ty3 + 1] == 0 and graph[tx5][ty5 + 1] == 0
                        and graph[tx3 + 1][ty3 + 1] == 0 and graph[tx2 + 1][ty2 + 1] == 0):
                    x1 = x1 + 1; y1 = y1 + 1
                    x2 = x2 + 1; y2 = y2 + 1
                    x3 = x3 + 1; y3 = y3 + 1
                    x4 = x4 + 1; y4 = y4 + 1
                    x5 = x5 + 1; y5 = y5 + 1
                    di = turn_cw(di)
                    continue
                else:  # 좌하단 우하단 둘다 이동 불가능 한 경우
                    break
            else:
                break
    if not inbound(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
        for i in range(r + 3):
            for j in range(c):
                graph[i][j] = 0
        path.clear()
        exit.clear()
        continue
    graph[x1][y1] = idx
    graph[x2][y2] = idx
    graph[x3][y3] = idx
    graph[x4][y4] = idx
    graph[x5][y5] = idx
    find_exit(exit, x4, y4, di)
    visited = [[False] * c for _ in range(r + 3)]
    path.clear()
    bfs(graph, visited, x4, y4)
    path.sort(key = lambda x: (-x[0], x[1]))
    fx, fy = path[0]
    ans += (fx + 1 - 3)
print(ans)