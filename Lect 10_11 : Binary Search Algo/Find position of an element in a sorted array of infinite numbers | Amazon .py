#same binary search code
def search(nums,target,si,ei):
	while si <= ei:
		mi = (si + ei) // 2
		if nums[mi] < target:
			si = mi + 1

		elif nums[mi] > target:
			ei = mi - 1

		else:
			return mi

	return -1

if __name__ == '__main__':
	arr = [1,2,4,6,7,8,9,10,14,16,17,22,24,26,29,30]
	
	# we dont know the end index hence apply binary search on chunk/bunch
	si = 1
	ei = 2 

	while True:
		# print(si-1,ei-1)
		val = search(arr,30,si-1,ei-1)
		if val != -1:
			print('index = ',val)
			break
		si = si * 2
		ei = ei * 2
