def quick_sort(arr,start=0,end=None):
    if end is None:
        arr=list(arr)
        end=len(arr)-1
    if start<end:
        pivot=partition(arr,start,end)
        quick_sort(arr,start,pivot-1)
        quick_sort(arr,pivot+1,end)
    return arr
def partition(arr,start,end):
    i,j=start,end-1
    while i<j:
        if arr[i]<=arr[end]:
            i+=1
        elif arr[j]>arr[end]:
            j-=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>arr[end]:
        arr[i],arr[end]=arr[end],arr[i]
        return i
    else:
        return end
print(quick_sort([65,32,4,32,8,46,97,23,53,22,12,7,0,98]))
