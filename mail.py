import random


def f4(a):
    global a1 , a2 , a3 , a4
    a1 = a // 1000
    a2 = a // 100 % 10
    a3 = a % 100 // 10
    a4 = a % 10


def chongfu(c1, c2, c3, c4):
    global mum
    mum = 0
    for ui in (c2, c3, c4):
        if ui == c1:
            mum += 1
    for uo in (c3, c4):
        if uo == c2:
            mum += 1
    if c3 == c4:
        mum += 1


def bijiao(l1, l2, l3, l4):
    global r, b
    r = 0
    b = 0
    if t1 == l1:
        r += 1
    if t2 == l2:
        r += 1
    if t3 == l3:
        r += 1
    if t4 == l4:
        r += 1
    for i in (t1, t2, t3, t4):
        for o in(l1, l2, l3, l4):
            if i == o:
                b += 1
    b = b - r

tr = True
while tr:
    target=random.randrange(10000)
    f4(target)
    t1=a1
    t2=a2
    t3=a3
    t4=a4
    chongfu(t1,t2,t3,t4)
    if mum>0:
        continue
    else:
        tr = False


def inmunber():
    global n1,n2,n3,n4
    run = True
    while run:
        num = input('4 numbers :')
        if len(num)==4:
            f4(int(num))
        else:
            num = input('Input again:')
        n1 = a1
        n2 = a2
        n3 = a3
        n4 = a4
        chongfu(n1,n2,n3,n4)
        if mum>0:
            print('You write wrong number,try again.')
            continue
        else:
            run = False


for time in range(1,9):
    print('Time:{}.Left:{}.'.format(time,8-time))
    inmunber()
    bijiao(n1,n2,n3,n4)
    if r ==4:
        print('You Win!!!!!The target is {}'.format(target))
        break
    else:
        print('{}A{}B.'.format(r,b))

    if time == 8:
        print('You lose!The target is {}'.format(target))
