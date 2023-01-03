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

# # 연습
# print('오늘 아침 %s시에 일어났습니다' %7)
# print('오늘 아침 %d시에 일어났습니다' %7)
# print('오늘 아침 {}시에 일어났습니다'.format(7))
# print('오늘 아침 {}시 {}분에 일어났습니다'.format(7,30))
# print('오늘 아침 {1}시 {0}분에 일어났습니다'.format(7,30))
# print('오늘 아침 {hour}시 {minute}분에 일어났습니다'.format(hour=7,minute=30))
# hour, minute = 7,30
# print(f'오늘 아침 {hour}시 {minute}분에 일어났습니다')


# [탈출 문자; escape]
# \n : 줄바꿈
# \" : "를 출력
# \\ : \를 출력
# \r : 커서를 맨 앞으로 이동해준다.(덮어쓰기)
# \b : backspace
# \t : tab

# print('엔\n터')
# print('\'따옴표 출력\'')
# print('\\ *^^* /')
# print('black pink\r1234567890')
# print('backk\b spacee\b') # 두번은 안되나...?
# print('t\ta\tb')

# quiz3

# Rule_1 : slicing보다 replace로 하는 것이 다른 주소에도 활용할 수 있고 좋을 것 같다
# Rule_2 : replace보다는 index로 .이 있는 부분을 찾아서 그 지점까지 slicing


# url = "http://daum.net"
# rule1 = url.replace('http://','')
# print(rule1)


# rule2 = rule1[:rule1.index('.')]
# print(rule2)

# rule3 = rule2[:3]+str(len(rule2))+str(rule2.count('e'))+'!'
# print(rule3)


# print('생성된 비밀번호는 {}입니다'.format(rule3))
# print(f'site \'{url}\' generated code is {rule3}')
# print('{}의 비밀번호는 {}입니다'.format(url,rule3))

# # [List] : 순서를 가지는 객체의 집합

# sub = ['kim', 'lee', 'park']
# print(sub)

# # 리스트에 추가하기
# sub.append('choi')
# print(sub)

# # 중간에 추가하기
# sub.insert(2, 'kang')
# print(sub)

# # 뒤 부터 하나씩 빼기
# print(sub.pop())
# print(sub)

# # 값의 개수 구하기
# sub.append('kim')
# print(sub.count('kim'))

# # 정렬하기
# sub.append('ann')
# print(sub)
# sub.sort()
# print(sub)

# # 정렬 순서 뒤집기
# sub.reverse()
# print(sub)

# # 리스트 속 내용 다 지우기
# sub.clear()
# print(sub)

# # 리스트 합치기
# mix = [True, 1, 'three', '한글']
# print(mix)
# sub.extend(mix)
# print(sub)


# # [Dictionary]
# my_dict={'a-1':'a', 'b-2':'b', 'c-3':'c'}

# print(my_dict.get('a'))
# # my_dict[]로 값을 출력하려할때는 값이 없을때 에러가 발생하고 프로그램이 끝나는 반면
# # my_dict.get()로 값을 출력하게 되면 값이 없더라도 'None'이 출력되고 다음 코드가 진행된다.

# print(my_dict.get('a', 'a 값이 없음'))
# # 출력 요청한 값이 없을 때 뒤 항목을 출력해준다

# print('a-1' in my_dict)
# print(4 in my_dict)
# # 'value' in my_dict : 값이 있으면 True, 없으면 False 출력


# # 딕셔너리 추가하거나 업데이트
# print(my_dict)
# my_dict['d-4'] = '새로운 값'
# my_dict['a-1'] = '업데이트된 값'
# print(my_dict)

# # 딕셔너리에서 값 제거하기
# del my_dict['a-1']
# print(my_dict)

# # 키들만, 값들만 출력
# print(my_dict.keys())
# print(my_dict.values())

# # ky, value 쌍으로 출력
# print(my_dict.items())

# # dictionary 초기화
# my_dict.clear()
# print(my_dict)

# [tuple] : 리스트와 달리 변경이 안된다. 속도가 빠르다

# [set] : 집합, 중복이 안되고 순서가 없다.




