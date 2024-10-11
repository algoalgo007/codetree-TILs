from collections import deque

r, c, k = list(map(int, input().split()))

graph = [[0] * c for _ in range(r + 3)]
ans = 0
exit = []
path = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

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
                visited[nx][ny] = True
                q.append((nx, ny))
            if (x, y) in exit and graph[nx][ny] != 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))

def in_bound(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
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

def find_exit(dir, x, y):
    ex = x + dx[dir]
    ey = y + dy[dir]
    exit.append((ex, ey))

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
        tx1, ty1 = x1, y1
        tx2, ty2 = x2, y2
        tx3, ty3 = x3, y3
        tx4, ty4 = x4, y4
        tx5, ty5 = x5, y5
        if tx2 + 1 >= r + 3:
            break
        if graph[tx1 + 1][ty1] == 0 and graph[tx2 + 1][ty2] == 0 and graph[tx3 + 1][ty3] == 0:
            x1, y1 = tx1 + 1, ty1
            x2, y2 = tx2 + 1, ty2
            x3, y3 = tx3 + 1, ty3
            x4, y4 = tx4 + 1, ty4
            x5, y5 = tx5 + 1, ty5
            continue
        else: # 아래로 내려가는거 불가능
            if ty1 - 1 >= 0: #왼쪽 가능
                if graph[tx1][ty1-1] == 0 and graph[tx2][ty2-1] == 0 and graph[tx5][ty5-1] == 0 and graph[tx1 + 1][ty1 - 1] == 0 and graph[tx2 + 1][ty2 - 1] == 0:
                    x1, y1 = tx1 + 1, ty1 - 1
                    x2, y2 = tx2 + 1, ty2 - 1
                    x3, y3 = tx3 + 1, ty3 - 1
                    x4, y4 = tx4 + 1, ty4 - 1
                    x5, y5 = tx5 + 1, ty5 - 1
                    di = (di - 1) % 4
                    continue
                else: # 왼쪽 아래 불가능
                    if ty3 + 1 < c: # 오른쪽 가능
                        if graph[tx2][ty2 + 1] == 0 and graph[tx3][ty3 + 1] == 0 and graph[tx5][ty5 + 1] == 0 and graph[tx2 + 1][ty2 + 1] == 0 and graph[tx3 + 1][ty3 + 1] == 0:
                            x1, y1 = tx1 + 1, ty1 + 1
                            x2, y2 = tx2 + 1, ty2 + 1
                            x3, y3 = tx3 + 1, ty3 + 1
                            x4, y4 = tx4 + 1, ty4 + 1
                            x5, y5 = tx5 + 1, ty5 + 1
                            di = (di + 1) % 4
                            continue
                        else: # 왼쪽 오른쪽 둘다 불가능
                            break
                    else:
                        break
            else:
                if ty3 + 1 < c:  # 오른쪽 가능
                    if graph[tx2][ty2 + 1] == 0 and graph[tx3][ty3 + 1] == 0 and graph[tx5][ty5 + 1] == 0 and \
                            graph[tx2 + 1][ty2 + 1] == 0 and graph[tx3 + 1][ty3 + 1] == 0:
                        x1, y1 = tx1 + 1, ty1 + 1
                        x2, y2 = tx2 + 1, ty2 + 1
                        x3, y3 = tx3 + 1, ty3 + 1
                        x4, y4 = tx4 + 1, ty4 + 1
                        x5, y5 = tx5 + 1, ty5 + 1
                        di = (di + 1) % 4
                        continue
                    else:  # 왼쪽 오른쪽 둘다 불가능
                        break
                else:
                    break
    if not in_bound(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
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
    find_exit(di, x4, y4)
    visited = [[False] * c for _ in range(r + 3)]
    path.clear()
    bfs(graph, visited, x4, y4)
    path.sort(key = lambda x: (-x[0], x[1]))
    fx, fy = path[0]
    ans += (fx - 2)
print(ans)