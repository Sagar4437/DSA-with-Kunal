def traingle(arr):
    if len(arr) < 1:
        return
    l1 = []
    for i in range(len(arr)-1):
        l1.append(arr[i]+arr[i+1])
    traingle(l1)
    print(arr)

traingle([1,2,3,4,5])
