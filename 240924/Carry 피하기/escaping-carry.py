from itertools import combinations

n = int(input())
arr = []
global ans
ans = 0
for _ in range(n):
    arr.append(int(input()))

def check(temp):
    array = []
    maximum = 0
    flag = True
    for i in range(len(temp)):
        tVal = str(temp[i])
        array.append(tVal[::-1])
        maximum = max(maximum, len(tVal))
    for i in range(1, maximum + 1):
        val = 0
        for j in range(len(array)):
            if len(array[j]) >= i:
                val += int(array[j][i-1])
                if val >= 10:
                    flag = False
                    break
    if flag:
        return len(temp)
    else:
        return -1

    
    
        

for i in range(1, n + 1):
    for c in combinations(arr, i):
        temp = []
        for j in c:
            temp.append(j)
        val = check(temp)
        ans = max(ans, val)
print(ans)