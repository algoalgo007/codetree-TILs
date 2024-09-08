n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
numbers = {}
for i in range(len(arr)):
    if arr[i] not in numbers:
        numbers[arr[i]] = 1
    else:
        numbers[arr[i]] += 1

for i in range(n):
    if k - arr[i] in numbers:
        numbers[arr[i]] -= 1
        ans += numbers[k-arr[i]]

print(ans)