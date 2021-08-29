class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr =[]
        i = 0
        while i<n:
            arr.append(nums[i])            
            arr.append(nums[n+i])
            i += 1
        return arr
