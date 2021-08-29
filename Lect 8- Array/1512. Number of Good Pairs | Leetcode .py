class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i] == nums[j]:
                    c +=1
                    
        return c
