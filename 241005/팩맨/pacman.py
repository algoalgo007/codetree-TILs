import copy

m,s = map(int, input().split())
graph = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0] * 4 for _ in range(4)]
move = []
sx, sy = map(int, input().split())
sx -= 1
sy -= 1


dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
ddx = [-1, 0, 1, 0]
ddy = [0, -1, 0, 1]
array = [1, 2, 3, 4]
numbers = [0, 0, 0]
route = [(), (), ()]

for _ in range(m):
  a, b, c = map(int, input().split())
  a -= 1
  b -= 1
  c -= 1
  graph[a][b].append(c)

def counterCCW(dir):
  if dir == 0:
    return 7
  else:
    return dir - 1
  
def permC(cnt, sx, sy, count):
  if sx < 0 or sy < 0 or sx >=4 or sy >= 4:
    return
  if (sx, sy) in route:
    return
  if cnt == 3:
    if len(graph[sx][sy]) > 0:
      count += len(graph[sx][sy])
    path = ""
    for i in range(3):
      path += str(numbers[i])
    move.append((int(path), count))
    if len(graph[sx][sy]) > 0:
      count -= len(graph[sx][sy])
    return
  if len(graph[sx][sy]) > 0:
      count += len(graph[sx][sy])
  for i in range(4):
    numbers[cnt] = array[i]
    route[cnt] = (sx, sy)
    nx = sx + ddx[i]
    ny = sy + ddy[i]
    if nx < 0 or ny < 0 or nx >=4 or ny >= 4:
      continue
    if (nx, ny) in route:
      continue
    permC(cnt + 1, nx, ny, count)
    
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
  # 냄새 옅어짐
  for i in range(4):
    for j in range(4):
      if smell[i][j] != 0:
        smell[i][j] -= 1
  # 상어 이동 (64가지)
  route = [(), (), ()]
  permC(0, sx, sy, 0)
  move.sort(key = lambda x: (-x[1], x[0]))
  path, aa = move[0]
  path = str(path)
  if len(graph[sx][sy]) > 0:
    graph[sx][sy].clear()
    smell[sx][sy] = 2
  for i in range(len(path)):
    num = int(path[i]) - 1
    sx += ddx[num]
    sy += ddy[num]
    if len(graph[sx][sy]) > 0:
      graph[sx][sy].clear()
      smell[sx][sy] = 2
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