def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left,right=merge_sort(arr[:mid]),merge_sort(arr[mid:])
    return merge(left,right)
def merge(arr1,arr2):
    i,j,merged=0,0,[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    return merged+arr1[i:]+arr2[j:]
print(merge_sort([4,34,2,7,5,9,7,6,45,23,3])
