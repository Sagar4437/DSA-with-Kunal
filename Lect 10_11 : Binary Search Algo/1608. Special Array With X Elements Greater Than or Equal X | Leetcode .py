class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n,-1,-1):
            c = 0
            for j in nums:
                if i <= j:
                    c += 1
            if i == c:
                return i
            
        return -1
        
