def binary_2d_search(matrix,target):
	r = 0
	c = len(matrix[0]) - 1

	while r < len(matrix) and c >= 0:
		if matrix[r][c] == target:
			return [r,c]

		elif matrix[r][c] < target:
			r += 1

		else:
			c -= 1

	return [-1,-1]

matrix = [[10,20,30],[40,50,60],[70,80,90]]
print(binary_2d_search(matrix,80))
