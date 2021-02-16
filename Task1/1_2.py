import math
def form(x):
    if(x < -26):
        c = 86*((math.tan(x)+(x**8)-43)**2)-6*(x**8)
    elif(x >= -26 and x < 12):
        c = 53*(((x**4)/6+x-37)**3)-(x**7)/69
    elif(x >= 12 and x < 84):
        c = 14*(x**2)+math.cos(x)
    elif(x >= 84 and x < 161):
        c = math.fabs((x**4))+(x**2)/87+20
    elif(x >= 161):
        c = math.tan(math.cos(x))+(x**2)+46
    return (c)

x=int(input('x= '))
c = form(x)
print('%.2e'%c)