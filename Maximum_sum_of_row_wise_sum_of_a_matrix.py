N,M=map(int,input().split())
a=[]
b=[]
for i in range(N):
    l=list(map(int,input().split()))
    a.append(l)
for i in a:
    b.append(sum(i))
print(max(b))