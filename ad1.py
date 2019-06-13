import math
import random

print("Enter square function:")
print("In format ax^2+bx+c dla a,b,c=R")
print("Enter (integer) a")
a = int(input())
print("Enter (integer) b")
b = int(input())
print("Enter (integer) c")
c = int(input())

delta=pow(b,2)-4* a*c
if delta < 0:
    delta = 0
    x1='absence delta negative'
    x2='absence delta negativr'
else:
    x1= (-b + math.sqrt(delta))/ (2*a)
    x2= (-b-math.sqrt(delta))/(2*a)
print("Square root x1:%r" %x1)
print("Square root x2:%r" %x2)