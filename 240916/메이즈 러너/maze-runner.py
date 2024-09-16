from collections import deque

n, m, k = map(int, input().split())
graph = []
people = deque()
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    people.append((a, b))
ex, ey = map(int, input().split())
ex -= 1
ey -= 1
graph[ex][ey] = -2 # 탈출구
ans = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move():
    global ans
    q = deque()
    for i in range(len(people)):
        x, y = people[i]
        q.append((x, y))
    people.clear()
    while q:
        x, y = q.popleft()
        temp = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if (graph[nx][ny] == 0 or graph[nx][ny] == -2) and (abs(nx-ex) + abs(ny-ey) < abs(x - ex) + abs(y - ey)):
                temp.append((nx, ny))
        if len(temp) == 0:
            people.append((x, y))
        else:
            temp.sort(key = lambda x: (x[0], x[1]))
            tx, ty = temp[0]
            ans += (abs(x-tx) + abs(y-ty))
            if tx == ex and ty == ey: # 탈출
                continue
            people.append((tx, ty))

def find():
    global ex, ey
    temp = []
    for i in range(n):
        for j in range(n):
            for k in range(1, n):
                if i + k < n and j + k < n: # 정사각형 만들 수 있는 경우
                    cnt = 0
                    flag = False
                    for l in range(len(people)):
                        px, py = people[l]
                        if i <= px <= i + k and j <= py <= j + k:
                            cnt += 1
                    if i <= ex <= i + k and j <= ey <= j + k:
                        flag = True
                    if cnt >= 1 and flag:
                        temp.append((k, i, j))
    temp.sort(key = lambda x: (x[0], x[1], x[2]))
    size, sx, sy = temp[0]
    tx, ty = sx + size, sy + size
    length = len(people)
    for i in range(length):
        px, py = people.popleft()
        if sx <= px <= tx and sy <= py <= ty:
            graph[px][py] = -1
        else:
            people.append((px, py))
        
    tempGraph = [[0] * n for _ in range(n)]
    idx = sx
    for j in range(sy, ty + 1):
        tt = []
        for i in range(tx, sx - 1, -1):
            tt.append(graph[i][j])
        for l in range(len(tt)):
            tempGraph[idx][sy + l] = tt[l]
        idx += 1
    for i in range(sx, tx + 1):
        for j in range(sy, ty + 1):
            if tempGraph[i][j] >= 1:
                tempGraph[i][j] -= 1
            graph[i][j] = tempGraph[i][j]
            if graph[i][j] == -1:
                people.append((i, j))
                graph[i][j] = 0
            if graph[i][j] == -2:
                ex = i
                ey = j

for _ in range(k):
    if len(people) == 0:
        break
    move()
    find()

print(ans)
print(ex + 1, ey + 1)