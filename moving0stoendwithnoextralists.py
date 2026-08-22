lst=list(map(int,input().split()))
n=len(lst)
i=-1
for ind in range(n):
  if(lst[ind]==0):
    i=ind
    break
if(i!=-1):
  for j in range(i+,n):
    if(lst[j]!=0):
      lst[i],lst[j]=lst[j],lst[i]
      i+=1
print(lst)
