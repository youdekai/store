
def main():
    print("请输入要构成三角形的三个数据：")
    a = int(input("第一个数："))
    b = int(input("第二个数："))
    c = int(input("第三个数："))
    if a >= b + c or b >= a + c or c >= a + b:
        print("两边之和小于第三边，不能构成三角形。")
    else:
        flag = 0
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
            print("能构成直角三角形！")
            flag = 1
        if a == b and b == c:
            print("能构成等边三角形！")
            flag = 1
        elif a == b or b == c or c == a:
            print("能构成等腰三角形！")
            flag = 1
        if flag == 0:
            print("能构成普通三角形！")

if __name__ == '__main__':
    main()