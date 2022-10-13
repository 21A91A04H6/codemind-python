import math
A,B,C=map(float,(input().split()))
s=(A+B+C)/2
area=(math.sqrt(s*(s-A)*(s-B)*(s-C)))
print(format(area,".2f"))