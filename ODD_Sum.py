N=int(input())
lst=map(int,input().split())
odd=[i for i in lst if i%2!=0]
print(sum(odd))