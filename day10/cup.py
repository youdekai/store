'''
    水杯：
        属性：高度，容积，颜色，材质
        行为：能存放液体
'''
class cup:
    __high=0.0
    __volume=0
    __color=""
    __texture=""

    def setHigh(self,high):
        self.__high=high
    def getHigh(self):
        return self.__high

    def setvolume(self,volume):
        self.__volume=volume
    def getvolume(self):
        return self.__volume

    def setcolor(self,color):
        self.__color=color
    def getcolor(self):
        return self.__color

    def settexture(self,texture):
        self.__texture=texture
    def gettexture(self):
        return self.__texture

    def yt(self):
        print("能存放",self.__volume,"毫升的液体")
    def liquid(self):
        print("高度",self.__high,"\n容积",self.__volume,"\n颜色",self.__color,"\n材质",self.__texture)

c=cup()
c.setHigh(10)
c.setvolume(300)
c.setcolor("白色")
c.settexture("玻璃")

c.liquid()
c.yt()





























