#Saxon
import self as self


class SAXON:
    length = None
    width = None
    height = None
    length1 = None
    width1 = None
    depth1 = None
    Result = None
    Result1 = None

    def __init__(self):
            length = float(input("Input the length of Room : "))
            width = float(input("Input the Width of Room : "))
            height = float(input("Input the Height of Room : "))
            self.Room(length, width, height)

            length1 = float(input("\nInput the length of Pool : "))
            width1 = float(input("Input the Width of Pool : "))
            depth1 = float(input("Input the Depth of Pool : "))
            self.Pool(length1, width, height)

            print("I am going to clean Room with ",self.Result," area and Pool width ",self.Result1," volume");


    def Room(self, a, b, c):
        self.Result =a * b * c

    def Pool(self, length, Width, Height):
        self.Result1 = length * Width * Height * 7.5



choice=None
print("***CLEANING WITH SAXON***")
print("*I am a Robotic Cleaner*")
print("I am going to clean your room and Pool")
print("Please input your Dimensions Respectively\n")

obj = SAXON()