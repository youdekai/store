list=[]
i=0
num=0
sum=0
while i<10:
    num=int(input("请输入一个数:"))
    sum+=num
    i+=1
    list.append(num)
print("这十个数的总和为：",sum)
print("平均数：",sum/10)
print("最大值：",max(list))