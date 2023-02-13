def snail(n, m):
    arr = [[0 for j in range(m)] for i in range(n)] #1
    row = 0 #2
    col = -1 #2
    cnt = 1 #3
    trans = 1 #4
    while n > 0 and m > 0: #5
        for j in range(m): #6
            col += trans
            arr[row][col] = cnt
            cnt += 1
        n -= 1 #7
        for i in range(n): #8
            row += trans
            arr[row][col] = cnt
            cnt += 1
        trans *= -1 #9
    return arr


arr = snail(7)
for i in arr:
    for j in i:
        print('%5d' %j , end=' ')
    print()

print('\n')
print(snail(4))
n=5
m=4
print([[0 for j in range(m)] for i in range(n)])