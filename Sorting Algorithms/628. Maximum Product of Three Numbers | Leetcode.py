class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max(nums)
        nums.pop(nums.index(max1))
        
        max2 = max(nums)
        nums.pop(nums.index(max2))
        
        max3 = max(nums)
        nums.pop(nums.index(max3))
        
        
        nums.extend([max1,max2,max3])
        
        min1 = min(nums)
        nums.pop(nums.index(min1))
        
        min2 = min(nums)
        nums.pop(nums.index(min2))



        return max(min1*min2*max1,max1*max2*max3)
