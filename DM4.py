
from math import sin

def f(alpha):
    angle=alpha*3.1415927/180
    return sin(angle)-angle/2


a=60
while abs(f(a))>1e-8:
    a+=1e-5

print(a," ",f(a))
