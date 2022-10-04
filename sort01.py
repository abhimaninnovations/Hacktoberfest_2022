arr=[1,1,0,1]
low=0
high=len(arr)-1
while low<=high:
  if arr[low]==0:
    low=low+1
  elif arr[high]==1:
    high=high-1
  elif arr[low]>arr[high]:
    arr[low],arr[high]=arr[high],arr[low]
    low=low+1
    high=high-1
  else:
    pass
print(arr)