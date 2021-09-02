class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        si = 0
        ei = len(nums)-1
        
        while si <= ei:
            summ = nums[si] + nums[ei]
            if summ < target:
                si += 1
                
            elif summ > target:
                ei -= 1
                
            else:
                return [si+1,ei+1]
                
