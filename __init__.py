import random

randint=random.randint(1,5)
print(randint)
num=5
i=0
while i<5:
    number=int(input("请输入一个金币："))
    if number > randint:
        num = num-1
        print("猜大了,继续猜,当前金币余额为：",num)
    elif number < randint:
        num = num-1
        print("猜小了,继续猜,当前金币余额为:",num)
    else:
        print("恭喜你，猜对了")
        break
# while i<3:
#     number = int(input("请输入一个金币："))
#     if number > randint:
#         num = num - 1
#         print("猜大了,继续猜,当前金币余额为：",num)
#     elif number < randint:
#         num = num-1
#         print("猜小了,继续猜,当前金币余额为:",num)
#     else:
#         print("恭喜你，猜对了")
#         break
    i=i+1