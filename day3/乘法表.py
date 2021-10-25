def NxN(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,"x",i,"=",(j*i),"\t",end="")
        print()
while True:
    chose=input("请输入N层乘法：")
    chose=int(chose)
    NxN(chose)



















