x=int(input())
s=x*x
z=0
t=0
while x:
    d=x%10
    x=x//10
    z=z*10+d
l=z*z
while(l):
    d=l%10
    l=l//10
    t=t*10+d
if t==s:
    print('True')
else:
    print('False')