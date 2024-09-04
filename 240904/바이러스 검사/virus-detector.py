ans = 0

n = int(input())
arr = list(map(int, input().split()))
x, y = map(int, input().split())

for i in range(n):
    arr[i] -= x
    ans += 1

for i in range(n):
    if arr[i] <= 0:
        continue
    else:
        ans += arr[i] // y
        if arr[i] % y != 0:
            ans += 1
print(ans)