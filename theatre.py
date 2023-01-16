def price(people, morning, soldier):
    try:
        if people>0:
            print('일반 : {}명 '.format(people))

        if morning>0:
            print('조조 : {}명 '.format(morning))

        if soldier>0:
            print('군인 : {}명 '.format(soldier))

        print('[가격 : {}원]'.format(people*10000 + morning*6000 + soldier*4000))
    except TypeError:
        print('숫자를 입력하세요')
