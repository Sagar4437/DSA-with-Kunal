class Solution:
    def findMin(self, arr: List[int]) -> int:
        si = 0
        ei = len(arr) - 1

        while si < ei:
            mi = (si+ei) // 2

            # if mid val is smaller than end value 
            # then we can eliminate part on right side of mid index
            if arr[mi] < arr[ei]:
                ei = mi

            # if mid val is bigger than end val 
            # then we have to eliminate entire left portion 
            # including mid index
            else:
                si = mi +1

        # at last we remain with only one element so return it
        # as there is only one element in array
        # arr[ei] == arr[si] we can return anything
        return arr[si]
