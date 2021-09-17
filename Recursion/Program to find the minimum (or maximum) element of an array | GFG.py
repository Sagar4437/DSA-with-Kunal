def findMax(arr):
    if len(arr) == 1:
        return arr[0]

    fv = arr[0]
    lv = findMax(arr[1:])

    return max(fv,lv)

def findMin(arr):
    if len(arr) == 1:
        return arr[0]

    fv = arr[0]
    lv = findMin(arr[1:])

    return min(fv,lv)
 

arr=[19,23,322,40,5,6]
print(findMax(arr))
