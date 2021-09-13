class Solution:
    def firstMissingPositive(self, arr: List[int]) -> int:
        i = 0
        while i < len(arr):
            
            ci = arr[i] - 1
            
            if arr[i] <= 0 or arr[i] > len(arr):
                i += 1
            elif arr[i] == arr[ci]:
                i += 1
                
            else:
                arr[i],arr[ci] = arr[ci], arr[i]
                
        # print(arr)
        for i in range(len(arr)):
            if i+1 != arr[i]:
                return i+1
        else:
            return len(arr)+1
