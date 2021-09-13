class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        i = 0
        while i < len(arr):

            ci = arr[i]-1
            if arr[i] > len(arr):
                i += 1
            elif arr[ci] == arr[i]:
                i += 1
            else:
                arr[i],arr[ci] = arr[ci], arr[i]
                
        return arr[-1]
