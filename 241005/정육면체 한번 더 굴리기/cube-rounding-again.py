from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
visited = [[False] * n for _ in range(n)]

dice = [0, 1, 5, 3, 4, 2, 6]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = 1
x = 0
y = 0
ans = 0

def rotateCW(dir):
  if dir == 3:
    return 0
  else:
    return dir + 1
  
def rotateCCW(dir):
  if dir == 0:
    return 3
  else:
    return dir - 1

def roll_dice(dir):
  if dir == 0:
    temp = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[6]
    dice[6] = dice[2]
    dice[2] = temp
  elif dir == 1:
    temp = dice[1]
    dice[1] = dice[4]
    dice[4] = dice[6]
    dice[6] = dice[3]
    dice[3] = temp
  elif dir == 2:
    temp = dice[1]
    dice[1] = dice[2]
    dice[2] = dice[6]
    dice[6] = dice[5]
    dice[5] = temp
  else:
    temp = dice[1]
    dice[1] = dice[3]
    dice[3] = dice[6]
    dice[6] = dice[4]
    dice[4] = temp

def counterDir(dir):
  if dir == 0:
    return 2
  elif dir == 1:
    return 3
  elif dir == 2:
    return 0
  else:
    return 1
  
def bfs(graph, visited, x, y):
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  cnt = 0
  while q:
    x, y = q.popleft()
    cnt += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      if graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
        q.append((nx, ny))
        visited[nx][ny] = True
  return cnt

for _ in range(m):
  nx = x + dx[dir]
  ny = y + dy[dir]
  if nx < 0 or ny < 0 or nx >= n or ny >= n: # 이동 방향을 반대로 한다음 굴러간다
    dir = counterDir(dir)
    nx = x + dx[dir]
    ny = y + dy[dir]
  roll_dice(dir)
  visited = [[False] * n for _ in range(n)]
  result = bfs(graph, visited, nx, ny)
  ans += (graph[nx][ny] * result)
  if dice[6] > graph[nx][ny]:
    dir = rotateCW(dir)
  elif dice[6] < graph[nx][ny]:
    dir = rotateCCW(dir)

  x = nx
  y = ny

print(ans)