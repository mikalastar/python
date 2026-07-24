
x=float(input(' x = '))
y=float(input(' y = '))

def echange(a,b):
    c=a
    a=b
    b=c
    return(a,b)

if x*y>0 :
   x , y = echange(x,y)

else:
    s=x+y
    p= x*y
    x=s
    y=p
    
print('x = ' , x)
print(' y = ',y)    
    