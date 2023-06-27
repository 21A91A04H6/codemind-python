N,M=map(int,input().split())
mat=[]
c=0
for i in range(N):
    l=list(map(int,input().split()))
    mat.append(l)
for i in mat:
    for j in i:
        c+=j
print(c)