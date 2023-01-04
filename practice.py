print(2**3)
print(5%3) # 5/3 값의 나머지
print(5//4) # 5/4의 몫
print('\n')
print(3==3) # 등호 역할
print(3!=4) # 부등호
print('\n')
print((3>0) and (3<5))
print((3>0) & (3<5))
print((3>5) or (1>0))
print((3>5) | (3>1))
print('\n')
print(5>4>3)
print('\n')
number = 17
number+=3 # number = number + 3
print(number)
number-=3 # number = number -3
print(number)
number *= 3 # number = number*3
print(number)
number /= 3 # number = number/3
print(number)
print('\n')
number%=5 # number = number%5
print(number)
number //= 5 # number = number // 5
print(number)
print('\n')
print(abs(-5)) # 절대값
print(pow(2,3)) # 제곱
print(max([1,2,3,4,5,6,7,8])) # 최대값
print(min(1,2)) # 최소값
print(round(2.14)) # 정수로 반올림

from math import *
print(ceil(2.14)) # 올림
print(floor(2.14)) # 내림

from random import *
print(random()) # [0.0,1.0) 랜덤한 값 생성
print(random() * 10)  # [0.0,10.0) 랜덤한 값 생성
print((int(random()*10))+1)  # [1,10] 랜덤한 값 생성
print(randrange(1,46)) # [1,46) 랜덤한 값 생성
print('random lottery number')
print(randint(1,45)) # [1,45] 랜덤한 값 생성
print(randint(1,45)) # [1,45] 랜덤한 값 생성
print(randint(1,45)) # [1,45] 랜덤한 값 생성
print(randint(1,45)) # [1,45] 랜덤한 값 생성
print(randint(1,45)) # [1,45] 랜덤한 값 생성
print(randint(1,45)) # [1,45] 랜덤한 값 생성

Quiz #2
off_date = randint(4,28)
print('오프라인 스터디 모임 날짜는 매월',str(off_date)+'일로 선정되었습니다')
python = 'Python is Amazing'

print(python.lower())  # 소문자로 변환
print(python.upper())  # 대문자로 변환
print(python[0].isupper())  # 대문자인가를 확인. 결과는 불린
print(len(python))  
print(python.replace("Python", "Java")) # 대체
index = python.index("n")
print(index)
index = python.index("n", index+1) # 검색 시작위치를 지정해줄 수도 있다
print(index)
print(python.find('n'))

print(python.find('Java'))  # .find()에서 원하는 값이 없을때는 -1을 출력
# print(python.index('Java'))  # .index()에서는 원하는 값이 없으면 에러 발생

print(python.count('n'))

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
age = 20
print(f'{age})

# 연습
print('오늘 아침 %s시에 일어났습니다' %7)
print('오늘 아침 %d시에 일어났습니다' %7)
print('오늘 아침 {}시에 일어났습니다'.format(7))
print('오늘 아침 {}시 {}분에 일어났습니다'.format(7,30))
print('오늘 아침 {1}시 {0}분에 일어났습니다'.format(7,30))
print('오늘 아침 {hour}시 {minute}분에 일어났습니다'.format(hour=7,minute=30))
hour, minute = 7,30
print(f'오늘 아침 {hour}시 {minute}분에 일어났습니다')


# [탈출 문자; escape]
# \n : 줄바꿈
# \" : "를 출력
# \\ : \를 출력
# \r : 커서를 맨 앞으로 이동해준다.(덮어쓰기)
# \b : backspace
# \t : tab

print('엔\n터')
print('\'따옴표 출력\'')
print('\\ *^^* /')
print('black pink\r1234567890')
print('backk\b spacee\b') # 두번은 안되나...?
print('t\ta\tb')

# quiz3

# Rule_1 : slicing보다 replace로 하는 것이 다른 주소에도 활용할 수 있고 좋을 것 같다
# Rule_2 : replace보다는 index로 .이 있는 부분을 찾아서 그 지점까지 slicing


url = "http://daum.net"
rule1 = url.replace('http://','')
print(rule1)


rule2 = rule1[:rule1.index('.')]
print(rule2)

rule3 = rule2[:3]+str(len(rule2))+str(rule2.count('e'))+'!'
print(rule3)


print('생성된 비밀번호는 {}입니다'.format(rule3))
print(f'site \'{url}\' generated code is {rule3}')
print('{}의 비밀번호는 {}입니다'.format(url,rule3))

# [List] : 순서를 가지는 객체의 집합

sub = ['kim', 'lee', 'park']
print(sub)

# 리스트에 추가하기
sub.append('choi')
print(sub)

# 중간에 추가하기
sub.insert(2, 'kang')
print(sub)

# 뒤 부터 하나씩 빼기
print(sub.pop())
print(sub)

# 값의 개수 구하기
sub.append('kim')
print(sub.count('kim'))

# 정렬하기
sub.append('ann')
print(sub)
sub.sort()
print(sub)

# 정렬 순서 뒤집기
sub.reverse()
print(sub)

# 리스트 속 내용 다 지우기
sub.clear()
print(sub)

# 리스트 합치기
mix = [True, 1, 'three', '한글']
print(mix)
sub.extend(mix)
print(sub)


# [Dictionary]
my_dict={'a-1':'a', 'b-2':'b', 'c-3':'c'}

print(my_dict.get('a'))
# my_dict[]로 값을 출력하려할때는 값이 없을때 에러가 발생하고 프로그램이 끝나는 반면
# my_dict.get()로 값을 출력하게 되면 값이 없더라도 'None'이 출력되고 다음 코드가 진행된다.

print(my_dict.get('a', 'a 값이 없음'))
# 출력 요청한 값이 없을 때 뒤 항목을 출력해준다

print('a-1' in my_dict)
print(4 in my_dict)
# 'value' in my_dict : 값이 있으면 True, 없으면 False 출력


# 딕셔너리 추가하거나 업데이트
print(my_dict)
my_dict['d-4'] = '새로운 값'
my_dict['a-1'] = '업데이트된 값'
print(my_dict)

# 딕셔너리에서 값 제거하기
del my_dict['a-1']
print(my_dict)

# 키들만, 값들만 출력
print(my_dict.keys())
print(my_dict.values())

# ky, value 쌍으로 출력
print(my_dict.items())

# dictionary 초기화
my_dict.clear()
print(my_dict)

# [tuple] : 리스트와 달리 변경이 안된다. 속도가 빠르다

# [set] : 집합, 중복이 안되고 순서가 없다.

a = ['박', '충', '호', '호', '영', '범']
b = ['강', '대', '음', '최', '호', '진']

c = {'박', '충', '호', '호', '영', '범'}
d = {'강', '대', '음', '최', '호', '진'}
e = ('이', '명', '렬', '박', '다', '한')

# 교집합 만들기
print(c&d)    # set 끼리만 &로 교집합할 수 있는 반면
print(c.intersection(e))   # set.intersection()의 경우 ()에 list,tuple,set 올 수 있다.

# 합집합
print(c|d)
print(c.union(d))    
print(c.union(e))    

# 차집합
print(c-d)
print(c.difference(e))

c.add('진')
print(c)

c.remove('진')
print(c)

# .add, .remove, .intersection, .union, .difference 는 set에서만 사용가능

# quiz4
from random import *
id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
chicken = sample(id,1)  # 치킨 당첨자 1명 무작위 추첨
snd_id = list(set(id) - set(chicken))  # 중복을 막기 위해 치킨 수령자를 id list에서 제거
coffee = sample(id,3)  # 커피 당첨자 3명 무작위 추첨

print(f''' -- 당첨자 발표 -- \n치킨 당첨자 : {chicken[0]}\n커피당첨자 : {coffee}\n -- 축하합니다 -- ''')


# 나도 코딩 답지
from random import *
user = list(range(1,21))  # [1:21) 숫자를 생성하여 ilst로 user에 저장
shuffle(user) # list 섞어주기
winners = sample(user, 4)  # 해당 리스트에서 네명을 무작위로 뽑는다.

print('\n -- 당첨자 발표 -- ')
print('치킨 당첨자 : {}'.format(winners[0]))
print('커피당첨자 : {}'.format(winners[1:]))
print(' -- 축하합니다 -- ')

# Q. .sample 에서 무작위로 추출할텐데 앞에서 굳이 shuufle()해줄 필요가 있었나?


# [분기]
time = int(input('what time is it now? (0000) '))
if time > 1200 & time < 1330:
    print('it\'s lunch time')
elif time < 900:
    print('you dont even start working')
elif time > 1800 :
    print('it\'s time to go home')
else:
    print('work hard!')

# [반복문, for]
for i in range(1,21):
    print(f'대기번호 : {i}')

[반복문, while] : 특정 조건이 만족할 때까지 반복
무한루프에 빠졌을 때 ctrl + C 누르면 빠져나올 수 있다.

# 5번 불렀는데 찾아가지 않으면 커피를 버린다
customer = '박충호'
i = 5
while i >= 1:
    i -=1
    print('{0}고객님 커피 찾아가세요~ (호출 횟수 {1}번 남았습니다)'.format(customer, i))
    if i ==0:
        print('커피 폐기')

# 부르고 이름 확인하고 이름이 맞을 때까지 부른다

customer = '박충호'
person = 'unknown'

while person != customer:
    print('{}고객님 커피 찾아가세요'.format(customer))
    person = input('고객 성함 입력 ')
    if person != customer:
        print('{}고객님이 아닙니다\n'.format(customer))
print('{}고개님 커피 수령 완료'.format(customer))


# [continue & break] 반복문 내에서 사용
# continue : 조건이 충족되면 아래 코드로 내려가지 않고 다시 위의 반복문으로 돌아간다. 
# break : 반복문을 깨고 나온다

absent = [2,9]
no_book = [6]

for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print('폐강')
        break
    else:
        print(student)

# [for문 한 줄 입력!]



