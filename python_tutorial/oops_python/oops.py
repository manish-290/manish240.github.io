#object oriented concepts in python

#lets craete the class Point:
class Point:
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

#here self is an obect to store the x cordiante and y cordinate

#lets create the object of Point
p = Point(3,4)
print(p.x)
print(p.y) 
        
#since p and self both are the objects