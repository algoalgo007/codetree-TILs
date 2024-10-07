dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ddx = [-1, -1, 1, 1]
ddy = [-1, 1, 1, -1]

n, m, k, c = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
medi = [[0] * n for _ in range(n)]
ans = 0

def grow():
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0: # 나무
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if graph[nx][ny] > 0 and medi[nx][ny] == 0:
                        cnt += 1
                graph[x][y] += cnt

def produce():
    temp = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0: # 나무
                cnt = 0
                pos = []
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if graph[nx][ny] == 0 and medi[nx][ny] == 0: # 빈칸
                        cnt += 1
                        pos.append((nx, ny))
                for a, b in pos:
                    temp[a][b] += graph[x][y] // cnt
    for i in range(n):
        for j in range(n):
            graph[i][j] += temp[i][j]

def find():
    temp = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0: # 나무
                cnt = 0
                for i in range(4):
                    tx = x
                    ty = y
                    for _ in range(k):
                        nx = tx + ddx[i]
                        ny = ty + ddy[i]
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            break
                        if graph[nx][ny] == -1:
                            break
                        if graph[nx][ny] > 0:
                            cnt += graph[nx][ny]
                        tx = nx
                        ty = ny
                temp[x][y] = cnt + graph[x][y]
    maximum = -1
    tPos = []
    for i in range(n):
        for j in range(n):
            if temp[i][j] > maximum:
                maximum = max(temp[i][j], maximum)
    for i in range(n):
        for j in range(n):
            if temp[i][j] == maximum:
                tPos.append((i, j))
    tPos.sort(key = lambda x: (x[0], x[1]))
    mx, my = tPos[0]
    medi[mx][my] = (c + 1)
    graph[mx][my] = 0
    for i in range(4):
        tx = mx
        ty = my
        for _ in range(k):
            nx = tx + ddx[i]
            ny = ty + ddy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                break
            if graph[nx][ny] == -1:
                break
            graph[nx][ny] = 0
            medi[nx][ny] = (c + 1)
    return maximum

def time():
    for i in range(n):
        for j in range(n):
            if medi[i][j] > 0:
                medi[i][j] -= 1

for _ in range(m):
    grow()
    produce()
    value = find()
    ans += value
    time()
print(ans)