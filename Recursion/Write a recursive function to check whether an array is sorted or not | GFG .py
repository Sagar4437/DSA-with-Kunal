def isSorted(arr):
    if len(arr) < 2:
        return True

    bigPart = isSorted(arr[1:])
    smallPart = arr[0]

    if bigPart and smallPart < arr[1]:
        return True
    else:
        return False

arr = [1,5,3,4]

print(isSorted(arr))
