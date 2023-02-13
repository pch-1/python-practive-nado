# 문제 3 / 4H

from itertools import *
# while True:
#     try:
#         N=int(input('동전의 개수를 입력하세요 : '))
#         unit=input('동전의 개수만큼 화폐 단위를 입력하세요(공백으로 구분) : ')
#         dataset= list(map(int, unit.split(' ')))    # 입력 받은 unit에서 ' '를 제거하면서(.split) 리스트로 바꾸로, int로 변환해줌( list(map()) )
#         if len(dataset) == N:   # 동전의 개수가 일치하는지 확인
#             break
#         else:
#             print('Error : 동전의 개수만큼 화폐 단위를 입력하였는지 확인해주세요\n')
#     except ValueError:
#         print('잘못된 값을 입력하였습니다.\n')



# 입력
N=int(input('동전의 개수를 입력하세요 : '))
unit=input('동전의 개수만큼 화폐 단위를 입력하세요(공백으로 구분) : ')
dataset= list(map(int, unit.split()))    # 입력 받은 unit에서 ' '를 제거

'''
dataset.sort()

target = 1
for i in dataset:
    if i > target:
        break
    else:
        target+=i
print('answer :', target)
'''


# 처리
sum_list=[]     # 합한 값을 모으기 위한 빈 리스트 생성
for i in range(N):
    printList = list(set(combinations(dataset, i+1)))   # dataset에서 i개를 뽑아 만들 수 있는 조합의 경우를 printList에 저장
    for j in range(len(printList)):     # i개씩 묶인 조합의 개수만큼 반복. 조합 내부 숫자들 합을 구해서 sum_list.append
        sum_list.append((sum(printList[j])))
sum_list=list(set(sum_list))


# 출력
cnt=1
try:
    for k in range(1000001):
        if sum_list[k]!= k+1:
            break
        else:
            cnt+=1
    print(cnt)
except IndexError:
    print(cnt)



