import math
def form(n,m):
    sum1=0
    sum2=0
    for i in range(n):
        for j in range(m):
            sum1+=86*((j+1)**2)-48*(i+1)
    for i in range(n):
        sum2+=64*((i+1)**2)+85*((i+1)**5)
    c=sum1-72*sum2
    return c
n = int(input('n= '))
m = int(input('m= '))
c = form(n, m)
print('%.2e'%c)

