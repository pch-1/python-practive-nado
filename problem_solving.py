N=int(input('자연수를 입력하세요. : '))
b=[[1]]


# for i in range(N):
#     b[1]



for i in range(N):
    next_num=b[0][0]
    cnt=0
    list_next=[]

    for j in range(len(b[i])):
        if next_num == b[i][j]:
            cnt+=1
        else:
            list_next.append(b[i][j-1])
            list_next.append(cnt)
            next_num = b[i][j]
            cnt=1

        if (j == (len(b[i])-1)) and (next_num ==b[i][len(b[i])-1]): # 마지막 숫자가 next_num과 일치할때 리스트에 추가하기 위해
            list_next.append(next_num)
            list_next.append(cnt)

    b.append(list_next)


for k in b:
    for l in range(len(k)):
        print(k[l], end=' ')
    print('')
