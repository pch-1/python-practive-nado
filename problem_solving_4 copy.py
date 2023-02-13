def snail(m,n):
    arr = [[0] * m for _ in range(n)]
    row = 0 #2
    col = -1 #2
    cnt = 1 #3
    trans = 1 #4
    while n > 0 and m > 0: #5
        for j in range(m): #6
            col += trans
            arr[row][col] = cnt``
            cnt += 1
        n -= 1
        m -= 1 #7
        for i in range(n): #8
            row += trans
            arr[row][col] = cnt
            cnt += 1
        trans *= -1 #9
    return arr




NM= list(map(int, input('').split(' ')))    

arr = snail(NM[0],NM[1])

for i in arr:
    for j in i:
        print(j , end=' ')
    print()

