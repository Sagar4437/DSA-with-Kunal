def bubbleSort(arr):
	# Bubble Sort or Sinking Sort or Exchange sort
	# to check if arr is sorted then return from function

	isSwapped = False

	# Iterate over entire loop with pointer i
	for i in range(0,len(arr)):

		# iterate over arr[1:unsorted index]
		for j in range(1,len(arr)-i):
			if arr[j] < arr[j-1]:

				# swapped
				arr[j], arr[j-1] = arr[j-1], arr[j]
				isSwapped = True

		if not isSwapped:
			break

def selectionSort(arr):
	# swap max or min element with its index position

	# Iterate over entire loop with pointer i
	l = len(arr) - 1
	while(l > 0):
		# find max index in arr
		i = arr.index(max(arr[0:l+1]))

		# swapped
		arr[i], arr[l] = arr[l], arr[i]

		l -= 1

def insertionSort(arr):
	'''
	Run from zero till len - 2 
		coz
			1) index start from zero hence reduce 1
			2) we not compare 1st element hence reduce 1 again
		thats why we reduce 2

	'''
	for i in range(0,len(arr)-1):

		#  run loop from current i index to 0 and place in correct position
		for j in range(i+1,0,-1):
			if arr[j] < arr[j-1]:

				arr[j], arr[j-1] = arr[j-1], arr[j]

			else:
				break

def cyclicSort(arr):
  '''

  ==> Cyclic sort is very imp
  ==> range(0,N) ---> alway use Cyclic Sort
  ==> Amazon VVVIMP

  ==> no -ve numbers should in arr
  ==> all elements should br unique. i.e. no repeting elements allowed
  ==> numbers should be continues 



  '''
	curr_index = 0
	while curr_index < len(arr):

		correct_index = arr[curr_index] - 1

		if curr_index != correct_index:

			arr[curr_index], arr[correct_index] = arr[correct_index], arr[curr_index]

		else:
			curr_index += 1


arr = [6,1,3,2,5,4]
cyclicSort(arr)
print(arr)
