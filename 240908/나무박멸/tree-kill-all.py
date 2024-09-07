from collections import deque

n, m, k, c = map(int, input().split())
graph = []
tree = []
medicine = [[0] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cx = [-1, -1, 1, 1]
cy = [-1, 1, 1, -1]
ans = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if graph[i][j] > 0:
            tree.append((i, j))

def growth():
    q = deque()
    for i in range(len(tree)):
        x, y = tree[i]
        q.append((x, y))
    length = len(q)
    for _ in range(length):
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] > 0 and medicine[nx][ny] == 0:
                cnt +=1
        graph[x][y] += cnt
    
def spread():
    next_graph = [[0] * n for _ in range(n)]
    q = deque()
    for i in range(len(tree)):
        x, y = tree[i]
        q.append((x, y))
    length = len(q)
    for _ in range(length):
        x, y = q.popleft()
        temp = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0 and medicine[nx][ny] == 0:
                temp.append((nx, ny))
        for i in range(len(temp)):
            tx, ty = temp[i]
            next_graph[tx][ty] += graph[x][y] // len(temp)
    for i in range(n):
        for j in range(n):
            graph[i][j] += next_graph[i][j]

def choice():
    global ans
    temp_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp_graph[i][j] = graph[i][j]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and graph[i][j] != -1:
                for t in range(4):
                    for l in range(1, k + 1):
                        nx = i + cx[t] * l
                        ny = j + cy[t] * l
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                        if graph[nx][ny] != -1:
                            temp_graph[i][j] += graph[nx][ny]
                        if graph[nx][ny] == 0 or graph[nx][ny] == -1:
                            break

    temp = []
    for i in range(n):
        for j in range(n):
            temp.append((temp_graph[i][j], i, j))
    temp.sort(key = lambda x: (-x[0], x[1], x[2]))

    temp_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp_graph[i][j] = graph[i][j]
    val, x, y = temp[0]
    ans += temp_graph[x][y]
    graph[x][y] = 0
    medicine[x][y] = (c + 1)

    for i in range(4):
        for j in range(1, k + 1):
            nx = x + cx[i] * j
            ny = y + cy[i] * j
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] != -1:
                ans += temp_graph[nx][ny]
                graph[nx][ny] = 0
                medicine[nx][ny] = (c + 1)
            if temp_graph[nx][ny] == 0 or temp_graph[nx][ny] == -1:
                break

for _ in range(m):
    growth()
    spread()
    choice()
    for i in range(n):
        for j in range(n):
            if medicine[i][j] > 0:
                medicine[i][j] -= 1
    tree = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                tree.append((i, j))

print(ans)