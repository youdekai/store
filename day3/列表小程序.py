import random
import time
list=["杨洋","白敬亭","王一博","肖战","马天宇","邢昭林","丁程鑫","马嘉祺","林一","尤德楷"]
while True:
    index = input("请输入1 or 2 or q or Q ")
    if index=="1":
        dint=random.randint(0,len(list)-1)
        print(list[dint])
    elif index=="2":
        num = random.randint(0, 10)
        print(list[dint], "处罚了", num, "遍")
    elif index=="q" or index=="Q":
        print("退出系统")
        break
    else:
        time.sleep(10)
