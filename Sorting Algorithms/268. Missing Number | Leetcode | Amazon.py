class Solution:
    '''
    as array is distinct with range 0 - N ---> use cyclic sort
    '''
    
    
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        
#       Cyclic sort algorithm
        while i < len(nums):
            correct_i = nums[i] 
            if correct_i >= len(nums):
                i += 1
                
            elif i != correct_i:
                nums[i], nums[correct_i] = nums[correct_i], nums[i]
                 
            else:
                i += 1
        
        for index,val in enumerate(nums):
            if val != index:
                return index
            
        else:
            return len(nums)
        
        
        
#   Approch 2nd
    def missingNumber1(self, nums: List[int]) -> int:
        for i in range(0,max(nums)+1):
            if i not in nums:
                return i
        else:
            return i+1
                
        
        
