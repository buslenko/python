import math
def form(n):
    if(n==0):
        return 7
    elif(n==1):
        return 10
    else:
        c = (1/51)*(form(n-2))+math.sin((form(n-1)))
        return (c)
n=int(input(''))
c=form(n)
print('%.2e'%c)