#1
import math
n = int(input())
print(math.radians(n))


#2
h = float(input())
a = float(input())
b = float(input())
area = 0.5*((a + b)*h) 
print("area:", area)  


#3
import math
n = int(input())
s = float(input())
area = (n * s**2) / (4 * math.tan(math.pi/n))
print("area", area)


#4
import math
b = float(input())
h = float(input())
area = b * h
print("area", area)