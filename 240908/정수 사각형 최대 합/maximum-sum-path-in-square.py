n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for j in range(1, n):
    graph[0][j] += graph[0][j-1]

for i in range(1, n):
    graph[i][0] += graph[i-1][0]

for i in range(1, n):
    for j in range(1, n):
        graph[i][j] += max(graph[i-1][j], graph[i][j-1])

print(graph[n-1][n-1])