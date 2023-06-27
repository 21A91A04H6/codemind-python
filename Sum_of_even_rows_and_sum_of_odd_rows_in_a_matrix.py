N,M=map(int,input().split())
mat=[]
for i in range(N):
    l=list(map(int,input().split()))
    mat.append(l)
c=0
d=0
for i in range(N):
    for j in range(M):
        if i%2==0:
            c+=mat[i][j]
        else:
            d+=mat[i][j]
print(c,d)