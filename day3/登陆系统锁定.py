
username="root"
password="admin"

i=0
while i<3:
    i=i+1
    input_user=input("请输入用户名：")
    input_pass=input("请输入密码：")
    if input_user==username and input_pass==password:
        print("登陆成功！")
        break
    else:
        print("登陆失败！")
        continue


