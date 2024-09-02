n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
m = int(input())
arr2 = []
for _ in range(m):
    arr2.append(int(input()))

arr2.sort()
ans = 0
ansArr = []
for i in range(n - m + 1):
    temp = []
    flag = True
    for j in range(i, i + m):
        temp.append(arr[j])
    temp.sort()
    val = temp[0] - arr2[0]
    for j in range(m):
        if temp[j] - arr2[j] != val:
            flag = False
            break
    if flag:
        ans += 1
        ansArr.append(i + 1)
print(ans)
for i in range(len(ansArr)):
    print(ansArr[i])