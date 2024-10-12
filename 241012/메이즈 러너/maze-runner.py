from collections import deque

n, m, k = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
square = []
ans = 0

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
people = deque()
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    people.append((a, b))
ex, ey = map(int, input().split())
ex -= 1
ey -= 1

def in_bound(x1, y1, x2, y2, x3, y3, x4, y4):
    if x1 < 0 or y1 < 0 or x1 >= n or y1 >= n:
        return False
    if x2 < 0 or y2 < 0 or x2 >= n or y2 >= n:
        return False
    if x3 < 0 or y3 < 0 or x3 >= n or y3 >= n:
        return False
    if x4 < 0 or y4 < 0 or x4 >= n or y4 >= n:
        return False
    return True

def find_square():
    for i in range(n):
        for j in range(n):
            idx = 0
            for l in range(n):
                idx += 1
                x1, y1 = i, j
                x2, y2 = i, j + idx
                x3, y3 = i + idx, j
                x4, y4 = i + idx, j + idx
                if not in_bound(x1, y1, x2, y2, x3, y3, x4, y4): # 정사각형이 원래 그래프 벗어나는 경우
                    break
                else: # 정사각형이 원래 그래프 내부에 있는 경우
                    flag1 = False # 사람이 한명이라도 사각형 내부에 존재하는지 여부
                    flag2 = False # 탈출구가 사각형 내부에 존재하는지 여부
                    for q in range(len(people)):
                        tx, ty = people[q]
                        if x1 <= tx <= x4 and y1 <= ty <= y4:
                            flag1 = True
                            break
                    if x1 <= ex <= x4 and y1 <= ey <= y4:
                        flag2 = True
                    if flag1 == True and flag2 == True:
                        square.append((idx, x1, y1))

def rotate(length, x, y):
    global ex, ey
    tempGraph = [[0] * (length + 1) for _ in range(length + 1)]
    a = x-1
    for j in range(length, -1, -1):
        a += 1
        b = y-1
        for i in range(length + 1):
            b += 1
            tempGraph[i][j] = graph[a][b]
    a = -1
    for i in range(x, x + length + 1):
        a += 1
        b = -1
        for j in range(y, y + length + 1):
            b += 1
            graph[i][j] = tempGraph[a][b]

    # 벽 내구도 1 감소
    for i in range(x, x + length + 1):
        for j in range(y, y + length + 1):
            if graph[i][j] > 0:
                graph[i][j] -= 1
    # 정사각형 내부 사람 90도 회전
    number = len(people)
    flag2 = False
    for _ in range(number):
        a, b = people.popleft()
        flag = False
        row = x - 1
        for j in range(y + length, y - 1, -1):
            row += 1
            col = y-1
            for i in range(x, x + length + 1):
                col += 1
                if flag2 == False and ex == row and ey == col: # 탈출구 회전
                    ex = i
                    ey = j
                    flag2 = True
                if a == row and b == col: # 사람이 이 안에 있는 경우 90도 회전
                    people.append((i, j))
                    flag = True
        if not flag:
            people.append((a, b))

for _ in range(k):
    if len(people) == 0:
        break
    # 참가자 이동
    length = len(people)
    for _ in range(length):
        x, y = people.popleft()
        possible = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0 and (abs(nx - ex) + abs(ny - ey)) < ((abs(x - ex) + abs(y - ey))):
                possible.append((nx, ny))
        if len(possible) == 0:  # 4방향 중 이동할 곳이 없는 경우
            people.append((x, y))
        else:  # 4방향 중 이동할 곳이 있는 경우
            px, py = possible[0]
            if px == ex and py == ey: # 이동한 곳이 탈출구 이면 탈출
                ans += 1
                continue
            else:
                ans += 1
                people.append((px, py))
    # 가장 작은 정사각형 찾기
    square.clear()
    find_square()
    square.sort(key = lambda x: (x[0], x[1], x[2]))
    length, xpos, ypos = square[0]
    rotate(length, xpos, ypos)

print(ans)
print(ex + 1, ey + 1)