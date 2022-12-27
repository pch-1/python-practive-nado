# print(2**3)
# print(5%3) # 5/3 값의 나머지
# print(5//4) # 5/4의 몫
# print('\n')
# print(3==3) # 등호 역할
# print(3!=4) # 부등호
# print('\n')
# print((3>0) and (3<5))
# print((3>0) & (3<5))
# print((3>5) or (1>0))
# print((3>5) | (3>1))
# print('\n')
# print(5>4>3)
# print('\n')
# number = 17
# number+=3 # number = number + 3
# print(number)
# number-=3 # number = number -3
# print(number)
# number *= 3 # number = number*3
# print(number)
# number /= 3 # number = number/3
# print(number)
# print('\n')
# number%=5 # number = number%5
# print(number)
# number //= 5 # number = number // 5
# print(number)
# print('\n')
# print(abs(-5)) # 절대값
# print(pow(2,3)) # 제곱
# print(max([1,2,3,4,5,6,7,8])) # 최대값
# print(min(1,2)) # 최소값
# print(round(2.14)) # 정수로 반올림

# from math import *
# print(ceil(2.14)) # 올림
# print(floor(2.14)) # 내림

# from random import *
# print(random()) # [0.0,1.0) 랜덤한 값 생성
# print(random() * 10)  # [0.0,10.0) 랜덤한 값 생성
# print((int(random()*10))+1)  # [1,10] 랜덤한 값 생성
# print(randrange(1,46)) # [1,46) 랜덤한 값 생성
# print('random lottery number')
# print(randint(1,45)) # [1,45] 랜덤한 값 생성
# print(randint(1,45)) # [1,45] 랜덤한 값 생성
# print(randint(1,45)) # [1,45] 랜덤한 값 생성
# print(randint(1,45)) # [1,45] 랜덤한 값 생성
# print(randint(1,45)) # [1,45] 랜덤한 값 생성
# print(randint(1,45)) # [1,45] 랜덤한 값 생성

# Quiz #2
# off_date = randint(4,28)
# print('오프라인 스터디 모임 날짜는 매월',str(off_date)+'일로 선정되었습니다')
# python = 'Python is Amazing'

# print(python.lower())  # 소문자로 변환
# print(python.upper())  # 대문자로 변환
# print(python[0].isupper())  # 대문자인가를 확인. 결과는 불린
# print(len(python))  
# print(python.replace("Python", "Java")) # 대체
# index = python.index("n")
# print(index)
# index = python.index("n", index+1) # 검색 시작위치를 지정해줄 수도 있다
# print(index)
# print(python.find('n'))

# print(python.find('Java'))  # .find()에서 원하는 값이 없을때는 -1을 출력
# # print(python.index('Java'))  # .index()에서는 원하는 값이 없으면 에러 발생

# print(python.count('n'))

# [문자 포맷 방법]
# (1)
# d : 정수
# s : 문자열(str) / 종류 상관없이 다 출력해주기도 함
# c : character(한 글자만 받겠다)

# (2)
# '{}'format()
# {}안에 숫자를 넣어줘서 특정 순서에 있는 항목을 출력해줄 수도 있다.
# {} 안에 변수를 넣어줘서 출력해줄 수도 있다. / '{age}'.format(age=20)

# (3)
# 미리 선언한 변수를 넣어주기
# age = 20
# print(f'{age})

# 연습
print('오늘 아침 %s시에 일어났습니다' %7)
print('오늘 아침 %d시에 일어났습니다' %7)
print('오늘 아침 {}시에 일어났습니다'.format(7))
print('오늘 아침 {}시 {}분에 일어났습니다'.format(7,30))
print('오늘 아침 {1}시 {0}분에 일어났습니다'.format(7,30))
print('오늘 아침 {hour}시 {minute}분에 일어났습니다'.format(hour=7,minute=30))
hour, minute = 7,30
print(f'오늘 아침 {hour}시 {minute}분에 일어났습니다')