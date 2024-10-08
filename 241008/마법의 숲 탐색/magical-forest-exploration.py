from collections import deque

r, c, k = map(int, input().split())
graph = [[0] * c for _ in range(r)]
exit = []
pos = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
path = []
ans = 0

def turnC(dir):
    if dir == 3:
        return 0
    else:
        return dir + 1

def turnCC(dir):
    if dir == 0:
        return 3
    else:
        return dir - 1

def direction(x, y, dir):
    exit.clear()
    if dir == 0:
        x -= 1
        y = y
    elif dir == 1:
        x = x
        y += 1
    elif dir == 2:
        x += 1
        y = y
    else:
        x = x
        y -= 1
    exit.append((x, y))

def bfs(graph, visited, x, y, path):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        path.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
            if (x, y) in pos and graph[nx][ny] != 0 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True

def inbound(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
    if x1 < 0 or y1 < 0 or x1 >= r or y1 >= c:
        return False
    if x2 < 0 or y2 < 0 or x2 >= r or y2 >= c:
        return False
    if x3 < 0 or y3 < 0 or x3 >= r or y3 >= c:
        return False
    if x4 < 0 or y4 < 0 or x4 >= r or y4 >= c:
        return False
    if x5 < 0 or y5 < 0 or x5 >= r or y5 >= c:
        return False
    return True

idx = 1
for _ in range(k):
    idx += 1
    ci, di = map(int, input().split())
    ci -= 1
    x1, y1 = -1, ci-1
    x2, y2 = 0, ci
    x3, y3 = -1, ci+1
    x4, y4 = -1, ci
    x5, y5 = -2, ci
    direction(x4, y4, di)
    while True:
        tx1, ty1 = x1 + 1, y1
        tx2, ty2 = x2 + 1, y2
        tx3, ty3 = x3 + 1, y3
        tx4, ty4 = x4 + 1, y4
        tx5, ty5 = x5 + 1, y5
        if tx2 >= r:
            break
        if graph[tx1][ty1] == 0 and graph[tx2][ty2] == 0 and graph[tx3][ty3] == 0: # 아래로 이동 가능
            x1, y1 = tx1, ty1
            x2, y2 = tx2, ty2
            x3, y3 = tx3, ty3
            x4, y4 = tx4, ty4
            x5, y5 = tx5, ty5
            direction(x4, y4, di)
        else: # 아래로 이동 불가능 한 경우
            tx1, ty1 = x1 + 1, y1 - 1
            tx2, ty2 = x2 + 1, y2 - 1
            tx3, ty3 = x3 + 1, y3 - 1
            tx4, ty4 = x4 + 1, y4 - 1
            tx5, ty5 = x5 + 1, y5 - 1
            if ty1 >= 0 and tx2 < r: # 왼쪽 아래로 이동 가능한 경우
                if (graph[tx1][ty1] == 0 and graph[tx2][ty2] == 0 and graph[tx5][ty5] == 0
                        and graph[tx1-1][ty1] == 0 and graph[tx2-1][ty2] == 0 and graph[tx5-1][ty5] == 0):  # 서쪽 이동 가능
                    x1, y1 = tx1, ty1
                    x2, y2 = tx2, ty2
                    x3, y3 = tx3, ty3
                    x4, y4 = tx4, ty4
                    x5, y5 = tx5, ty5
                    di = turnCC(di)
                    direction(x4, y4, di)
                else: # 동쪽 아래로 이동
                    tx1, ty1 = x1 + 1, y1 + 1
                    tx2, ty2 = x2 + 1, y2 + 1
                    tx3, ty3 = x3 + 1, y3 + 1
                    tx4, ty4 = x4 + 1, y4 + 1
                    tx5, ty5 = x5 + 1, y5 + 1
                    if ty3 < c and tx2 < r: # 동쪽 이동 가능한 경우
                        if (graph[tx3][ty3] == 0 and graph[tx2][ty2] == 0 and graph[tx5][ty5] == 0
                            and graph[tx3-1][ty3] == 0 and graph[tx2-1][ty2] == 0 and graph[tx5-1][ty5] == 0):  # 동쪽 이동 가능
                            x1, y1 = tx1, ty1
                            x2, y2 = tx2, ty2
                            x3, y3 = tx3, ty3
                            x4, y4 = tx4, ty4
                            x5, y5 = tx5, ty5
                            di = turnC(di)
                            direction(x4, y4, di)
                        else: # 동쪽 아래로 이동 불가능 한 경우
                            break
                    else:
                        break
            else: # 서쪽 아래로 불가능
                tx1, ty1 = x1 + 1, y1 + 1
                tx2, ty2 = x2 + 1, y2 + 1
                tx3, ty3 = x3 + 1, y3 + 1
                tx4, ty4 = x4 + 1, y4 + 1
                tx5, ty5 = x5 + 1, y5 + 1
                if ty3 < c and tx2 < r:  # 동쪽 아래로 이동 가능한 경우
                    if (graph[tx3][ty3] == 0 and graph[tx2][ty2] == 0 and graph[tx5][ty5] == 0
                            and graph[tx3 - 1][ty3] == 0 and graph[tx2 - 1][ty2] == 0 and graph[tx5 - 1][ty5] == 0):  # 동쪽 이동 가능
                        x1, y1 = tx1, ty1
                        x2, y2 = tx2, ty2
                        x3, y3 = tx3, ty3
                        x4, y4 = tx4, ty4
                        x5, y5 = tx5, ty5
                        di = turnC(di)
                        direction(x4, y4, di)
                    else:  # 동쪽 아래로 이동 불가능 한 경우
                        break
                else:
                    break
    if not inbound(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
        for i in range(r):
            for j in range(c):
                graph[i][j] = 0
        pos.clear()
        path.clear()
        continue
    graph[x1][y1] = idx
    graph[x2][y2] = idx
    graph[x3][y3] = idx
    graph[x4][y4] = idx
    graph[x5][y5] = idx
    direction(x4, y4, di)
    ex, ey = exit[0]
    pos.append((ex, ey))
    visited = [[False] * c for _ in range(r)]
    path.clear()
    bfs(graph, visited, x4, y4, path)
    path.sort(key = lambda x: (-x[0], x[1]))
    fx, fy = path[0]
    ans += (fx + 1)

print(ans)