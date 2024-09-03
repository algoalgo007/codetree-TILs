n = int(input())
arr = [0] * 200001

for _ in range(n):
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b] -= 1

temp = 0
ans = 0
for i in range(1, 200001):
    temp += arr[i]
    ans = max(ans, temp)
print(ans)