import math
def form(x, y, z):
    c = (math.sqrt(86*(y**2)-48*y)+(z**3)+(z**7)+84+(z++4)+75*(x**6)+5)
    return (c)
x=int(input('x= '))
y=int(input('y= '))
z=int(input('x= '))
c=form(x, y, z)
print('%.2e'%c)