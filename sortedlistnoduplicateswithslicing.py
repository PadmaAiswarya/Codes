lst=list(map(int,input().split()))
n=len(lst)
i=0
for j in range (1,n):
  if(lst[i]!=lst[j]):
    lst[i+1]=lst[j]
    i+=1
print(lst[0:i+1])
