class Solution:
    def search(self,nums,target,first_occ = True):
        si = 0
        ei = len(nums) - 1
        ans = -1
        
        while si <= ei:
            mi = (si + ei) // 2
            
            if nums[mi] == target:
                ans = mi
                if first_occ:
                    ei = mi - 1
                else:
                    si = mi + 1
            elif nums[mi] < target:
                si = mi + 1

            else:
                ei = mi - 1
                
        return ans
                
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        
        first = self.search(nums,target,True)
        last = self.search(nums,target,False)
        ans[0] = first
        ans[1] = last
        
        return ans
       
