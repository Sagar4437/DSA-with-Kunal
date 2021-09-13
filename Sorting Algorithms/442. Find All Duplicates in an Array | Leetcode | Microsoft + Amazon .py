class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        i = 0
        while i < len(arr):

            ci = arr[i]-1
            if arr[i] > len(arr):
                i += 1
            elif arr[ci] == arr[i]:
                i += 1
            else:
                arr[i],arr[ci] = arr[ci], arr[i]
                
        r = []
        for i in range(len(arr)):
            if i+1 != arr[i]:
                r.append(arr[i])
        return r
        
        
