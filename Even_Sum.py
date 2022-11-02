n=int(input())
lst=map(int,input().split())
evens=(i for i in lst if i%2==0)
print(sum(evens))