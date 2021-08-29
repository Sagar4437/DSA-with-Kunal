class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for n in range(len(nums)):
            arr.insert(index[n],nums[n])
            
        return arr
