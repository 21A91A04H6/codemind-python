n=input()
a=[]
for i in n:
    if n.count(i)==1 and i not in a:
        a.append(i)
if len(a)==len(n):
    print("True")
else:
    print("False")