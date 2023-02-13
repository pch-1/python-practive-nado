# 문제 2 /1H

# 입력
NM=input('N M : ')
unit=input('N개의 수로 이루어진 수열 입력(공백으로 구분) : ')

# 전처리
NM=list(map(int, NM.split(' ')))
N=NM[0]
M=NM[1]
dataset=list(map(int, unit.split(' ')))    

# 연속부분수열 생성
seq_list=[]
for i in range(N):
    for j in range(N-i):
        try:
            seq_list.append(dataset[j:j+(i+1)])
        except IndexError:
            seq_list.append(dataset[-(i+1):])

# 개수 세기
cnt=0            
for i in range(len(seq_list)):
    if sum(seq_list[i])<=M:
        cnt+=1
print(cnt)





