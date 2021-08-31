def pivot(arr):
	si = 0 
	ei = len(arr) - 1

	if arr[0] > arr[ei]:
		while(si != ei):
			mi = (si+ei) // 2 

			if mi < len(arr) and arr[mi] > arr[mi+1]:
				ei = mi
				break

			elif mi > 0 and arr[mi] < arr[mi-1]:
				ei = mi - 1
				break

			elif arr[0] > arr[mi]:
				ei = mi - 1

			elif arr[0] < arr[mi]:
				si = mi + 1
		return ei 
	else:
		return -1

def binarySearch(arr,target,si,ei):
	while(si <= ei):
		mi = (si+ei) // 2
		if arr[mi] == target:
			return mi

		elif arr[mi] < target:
			si = mi + 1

		else:
			ei = mi - 1

	return -1

def RBS(arr,target):
	val = pivot(arr)

	if val == -1:
		return binarySearch(arr,target,0,len(arr)-1)

	if target <= arr[0]:
		return binarySearch(arr,target,val+1,len(arr)-1)

	else:
		return binarySearch(arr,target,0,val)


if __name__ == '__main__':
	arr = [3,4,5,6,1,2]
	target = 1

	ans = RBS(arr,target)
	print(ans)
