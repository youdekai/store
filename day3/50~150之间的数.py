import random
randint=random.randint(50,150)
print(randint)
i=0
while i<10:
    num=int(input("请输入您猜的数字："))
    if num==randint:
        print("猜对了")
        break
    elif num>randint:
        print("猜大了，继续猜吧！")
    elif num<randint:
        print("猜小了，继续猜吧！")
    else:
        print("猜错了，继续猜吧！")
    i=i+1