class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        elif nums[-1] < target:
            return len(nums)
        
        elif nums[0] > target:
            return 0
        
        else:
            si = 0
            ei = len(nums) - 1
            
            while si <= ei:
                mi = (si + ei) // 2
                if nums[mi-1] < target and target < nums[mi]:
                    return mi
                elif nums[mi] <= target:
                    si = mi + 1
                else:
                    ei = mi - 1
                    
                    
