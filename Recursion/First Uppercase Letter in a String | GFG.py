def firstUpperLetter(arr,si):
    ei = len(arr)
    if si == ei:
        return si if ord(arr[0]) < 97 else -1

    fv = arr[si]
    lv = firstUpperLetter(arr,si+1)

    if ord(fv) < 97 :
        return si
    else:
        return lv



arr="sagaRdaradE"

print(firstUpperLetter(arr,0))
