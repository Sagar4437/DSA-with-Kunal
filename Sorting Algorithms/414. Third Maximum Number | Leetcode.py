class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        
        i = 0
        arr = []
        
        for i in nums:
            if i not in arr:
                arr.append(i)
                
        if len(arr) < 3:
            return max(arr)
        
        arr.sort()
        return arr[-3]
