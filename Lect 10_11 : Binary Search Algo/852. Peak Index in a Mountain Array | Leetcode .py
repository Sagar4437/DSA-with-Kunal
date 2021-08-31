class Solution:
    #same binary search code
    def search(self,nums):
        si = 1
        ei = len(nums) - 1
        while si != ei:
            mi = (si + ei) // 2

            if nums[mi] > nums[mi + 1]:
                ei = mi

            elif nums[mi] < nums[mi + 1]:
                si = mi + 1

        return si
    
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        result = self.search(arr)
        
        return result
        
