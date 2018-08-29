import math
import tkinter

# 建議 類別定義 以 大寫字母開頭
class Circle:

    # initial a new object
    def __init__(self, raidus = 1):
        self.__radius = raidus


    def getRadius(self):
        return self.__radius
    
    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    

