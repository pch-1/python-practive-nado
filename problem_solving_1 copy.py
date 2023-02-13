# 문제 1 

n = int(input("정수를 입력하시오: "))

str1 = "1"

for i in range(0, n):
    prev = ""
    tmp = ""
    cnt = 0
    # notice: string도 for 가능.
    for s in str1:
        if prev != "" and prev != s:
            tmp += prev + str(cnt)
            cnt = 1
        else:
            cnt += 1
        prev = s
        
    tmp += prev + str(cnt)
    str1 = tmp
    print(str1)

