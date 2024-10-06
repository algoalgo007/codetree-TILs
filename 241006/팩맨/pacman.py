import copy

m,s = map(int, input().split())
graph = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0] * 4 for _ in range(4)]
move = []
visited = [[False] * 4 for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
ddx = [-1, 0, 1, 0]
ddy = [0, -1, 0, 1]
array = [1, 2, 3, 4]
numbers = [0, 0, 0]
sx, sy = map(int, input().split())
sx -= 1
sy -= 1

for _ in range(m):
  a, b, c = map(int, input().split())
  a -= 1
  b -= 1
  c -= 1
  graph[a][b].append(c)

def counterCCW(dir):
  if dir == 7:
    return 0
  else:
    return dir + 1
  
def permC(cnt, sx, sy, count, visited):
  if cnt == 3:
    pos = ""
    for i in range(3):
      pos += str(numbers[i])
    pos = int(pos)
    move.append((pos, count))
    return
  for i in range(4):
    nx = sx + ddx[i]
    ny = sy + ddy[i]
    if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
      continue
    if not visited[nx][ny]:
      visited[nx][ny] = True
      numbers[cnt] = (i + 1)
      count += len(graph[nx][ny])
      permC(cnt + 1, nx, ny, count, visited)
      visited[nx][ny] = False
      count -= len(graph[nx][ny])
    else:
      numbers[cnt] = (i + 1)
      permC(cnt + 1, nx, ny, count, visited)

for _ in range(s):
  move = []
  copyGraph = copy.deepcopy(graph)
  tempGraph = [[[] for _ in range(4)] for _ in range(4)]
  # 물고기 이동
  for i in range(4):
    for j in range(4):
      length = len(graph[i][j])
      for k in range(length):
        x = i
        y = j
        d = graph[i][j][k]
        for o in range(8):
          nx = x + dx[d]
          ny = y + dy[d]
          if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            d = counterCCW(d)
            continue
          if nx == sx and ny == sy:
            d = counterCCW(d)
            continue
          if smell[nx][ny] != 0:
            d = counterCCW(d)
            continue
          x = nx
          y = ny
          break
        tempGraph[x][y].append(d)
  for i in range(4):
    for j in range(4):
      graph[i][j] = tempGraph[i][j]
  # 상어 이동 (64가지)
  visited = [[False] * 4 for _ in range(4)]
  permC(0, sx, sy, 0, visited)
  move.sort(key = lambda x: (-x[1], x[0]))
  path, aa = move[0]
  path = str(path)
  for i in range(len(path)):
    num = int(path[i]) - 1
    sx += ddx[num]
    sy += ddy[num]
    if len(graph[sx][sy]) > 0:
      graph[sx][sy].clear()
      smell[sx][sy] = 3
  # 냄새 옅어짐
  for i in range(4):
    for j in range(4):
      if smell[i][j] != 0:
        smell[i][j] -= 1
  # 복제 마법
  for i in range(4):
    for j in range(4):
      for k in range(len(copyGraph[i][j])):
        graph[i][j].append(copyGraph[i][j][k])

ans = 0
for i in range(4):
  for j in range(4):
    ans += len(graph[i][j])
print(ans)