import  random

shop=[
    ["联想电脑", 6000],
    ["Iphone 16x plus", 15000],
    ["ps5游戏机", 3500],
    ["老干妈", 7.5],
    ["老于妈", 5.5]
]
#初始化余额
money=random.randint(0,99999)
print(money)

#购物车
mycart=[]

#展示商品
while False==0:
    for index,value in enumerate(shop):
        print(index,":",value)
    chose=input("请输入商品编号")
    if chose.isdigit():
        chose=int(chose)
        if chose <len(shop):
            if money>shop[chose][1]:
                mycart.append(shop[chose])
                money=money-shop[chose][1]
                print("恭喜你成功加入购物车，您的余额为：",money)
            else:
                print("gun")
        else:
            print("没有此商品")
    elif chose=="q"or chose=="Q":
        print("=================")
        for index, value in enumerate(mycart):
            print(index, ":", value)
        print("您的余额为：",money)
        break
    else:
        print("别瞎弄")
