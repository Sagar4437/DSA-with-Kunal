# Q: https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/

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

def index(arr,target):
	# we dont know the end index hence apply binary search on chunk/bunch
	si = 0
	ei = 1
	while target > arr[ei]:
		new_si = ei + 1

		# new_end = prev_end + box_size * 2
		ei = ei + (ei - si + 1)*2
		si = new_si

	return search(arr,target,si,ei)

if __name__ == '__main__':
	arr = [1,2,4,6,7,8,9,10,14,16,17,22,24,26,29,30]
	target = 22
	print(index(arr,target))
