def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
tests=[{
    "input": {
        "arr": [3,42,6,4,53,5,64,54,7]
        },
    "output":[3,4,5,6,7,42,53,54,64]
    },
    {
    "input": {
        "arr": []
        },
    "output":[]
    },
    {
    "input": {
        "arr": [4,3,42,6,4,4,4,4,53,5,64,4,54,7]
        },
    "output":[3,4,4,4,4,4,4,5,6,7,42,53,54,64]
    },
    {
    "input": {
        "arr": [3,3,3,3,3,3,3,3,3,3]
        },
    "output":[3,3,3,3,3,3,3,3,3,3]
    },
    {
    "input": {
        "arr": [6]
        },
    "output":[6]
    }]
i=0
for test in tests:
    if bubble_sort(**test['input'])==test['output']:
        print("Test",i,"Passed")
    else:
        print("Test",i,"Failed")
    i+=1
