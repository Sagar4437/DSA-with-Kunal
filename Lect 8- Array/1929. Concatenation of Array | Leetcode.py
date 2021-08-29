class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [nums[j] for i in range(2) for j in range(len(nums))]
        
