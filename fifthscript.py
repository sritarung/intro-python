#Sri Tarun Gulumuru
#duration: 60 mins
#Question5
import math
def rightTriangle(x1,y1,x2,y2,x3,y3):
    a = math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))
    b = math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))
    c = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

    if(math.sqrt(a*a+b*b)==c or math.sqrt(b*b+c*c)==a or math.sqrt(a*a+c*c)==b):
        return True
    else:
        return False

def equilateralTriangle(x1,x2,y1,y2,x3,y3):
    a = math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))
    b = math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))
    c = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

    if round(a,1)==round(b,1)==round(c,1):#rounding to one decimal point 
        return True
    else:
        return False

print('Enter the 3 points for the triangle')
print('Point 1')
x1 = float(input('Enter x: '))
y1 = float(input('Enter y: '))
print('Point 2')
x2 = float(input('Enter x: '))
y2 = float(input('Enter y: '))
print('Point 3')
x3 = float(input('Enter x: '))
y3 = float(input('Enter y: '))

print("Right Triangle", rightTriangle(x1,y1,x2,y2,x3,y3))
print("Equilateral Triangle", equilateralTriangle(x1,x2,y1,y2,x3,y3))
