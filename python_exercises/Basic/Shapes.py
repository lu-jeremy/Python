import math
def rectangle():
     print("Give me the height.")
     height=int(input())
     print("Give me the base.")
     base=int(input())
     area=base*height
     print(area)
     return area
def triangle():
     print("Give me the height.")
     height=int(input())
     print("Give me the base.")
     base=int(input())
     area=1/2*(base*height)
     print(area)
     print("Area=1/2(base x height)")
     return area
def circle():
    print("Give me the radius.")
    radius=int(input())
    area=math.pi*(radius*radius)
    print(area)
    print("Area=pir^2")
    return area

