def findCeilingNo(arr,n):
	si = 0
	ei = len(arr)-1
	while si <= ei:
		mi = (si + ei) // 2

		if arr[mi] == n:
			return mi

		elif arr[mi] < n:
			si = mi + 1

		else:
			ei = mi - 1

	return si



if __name__ == '__main__':
	arr = [1000,2000,3000,4000,5000]
	target = 3005 

	index = findCeilingNo(arr,target)

	print(arr[index])
