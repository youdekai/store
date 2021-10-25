def NxN(n):
    for i in range(1,n+1):
        print(" " * (n-i),"* " * i)
n=int(input("请输入要打印的行数："))
NxN(n)