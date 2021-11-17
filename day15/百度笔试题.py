f = open(file='baidu_x_system.log', mode='r+')
list = []
dict = {}
while True:
    content = f.readline()
    c = content.split(' ')
    if c == ['']:
        break
    list.append(c[0])
for i in list:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

print(dict)




# from collections import Counter
#
# index = open(file="baidu_x_system.log", mode="r+")
# print(index.readlines()[0])
# ff = dict(Counter(index.readlines()))
# # 只展示重复元素
# print([key for key, value in ff.items() if value > 1])
# print({key: value for key, value in ff.items() if value > 1})
