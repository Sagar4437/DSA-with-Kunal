def bubbleSort(arr):
    if len(arr) <= 1:
        return 

    for i in range(len(arr)-1):
        if arr[i]> arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    bubbleSort(arr[:-1])


arr=[2,5,3,4,7,8]
bubbleSort(arr)
print(arr)
