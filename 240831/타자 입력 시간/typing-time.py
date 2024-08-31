left, right = input().split()

leftArr = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']
rightArr = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm']

temp = 0
arr = []
arr.append(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
arr.append(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
arr.append(['z', 'x', 'c', 'v', 'b', 'n', 'm'])

lx, ly = -1, -1
rx, ry = -1, -1

for i in range(3):
    for j in range(len(arr[i])):
        if arr[i][j] == left:
            lx = i
            ly = j
        if arr[i][j] == right:
            rx = i
            ry = j

word = input()
for i in range(len(word)):
    if word[i] in leftArr:
        for j in range(3):
            for k in range(len(arr[j])):
                if word[i] == arr[j][k]:
                    temp += (abs(lx - j) + abs(ly - k))
                    temp += 1
                    lx = j
                    ly = k
    else:
        for j in range(3):
            for k in range(len(arr[j])):
                if word[i] == arr[j][k]:
                    temp += (abs(rx - j) + abs(ry - k))
                    temp += 1
                    rx = j
                    ry = k
print(temp)