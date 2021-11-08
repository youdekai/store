'''
电脑
    属性：屏幕大小  价格   cpu 型号  内存大小  待机时长
    行为：打字   打游戏   看视频
'''
class computer:
    __username=""
    __screenSize=0
    __price=0
    __cpu=""
    __memorySize=0
    __time=0

    def set_username(self,username):
        self.__username=username
    def get_username(self):
        return self.__username

    def set_screenSize(self, screenSize):
        self.__screenSize = screenSize
    def get_screenSize(self):
        return self.__screenSize

    def set_price(self, price):
        self.__price = price
    def get_price(self):
        return self.__price

    def set_cpu(self, cpu):
        self.__cpu = cpu
    def get_cpu(self):
        return self.__cpu

    def set_memorySize(self, memorySize):
        self.__memorySize = memorySize
    def get_memorySize(self):
        return self.__memorySize

    def set_time(self, time):
        self.__time = time
    def get_memorySize(self):
        return self.__time

    def type(self,typename):
        print(self.__username,"有",typename,"功能")
    def game(self,playGame):
        print(self.__username,"有",playGame,"功能")
    def video(self,Lookvideo):
        print(self.__username,"还有",Lookvideo,"功能")
    def introduce(self):
        print(self.__username,"屏幕大小为",self.__screenSize,"价格为",self.__price,"cpu型号",self.__cpu,"内存大小",self.__memorySize,"待机时长",self.__time)

c=computer()
c.set_username("戴尔")
c.set_screenSize("13-13.9英寸")
c.set_price(6000)
c.set_cpu("I5处理器")
c.set_memorySize("16G")
c.set_time("3小时")

c.type("打字")
c.game("打游戏")
c.video("看视频")
c.introduce()