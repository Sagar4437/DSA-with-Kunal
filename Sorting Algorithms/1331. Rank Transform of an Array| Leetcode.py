class Solution:
    def arrayRankTransform(self, nums: List[int]) -> List[int]:
        '''
        time = O(n)
        space = O(n)
        '''    
    
        arr = sorted(nums)
        ans = {}
        rank = 1
        for i in range(len(arr)):
            prev = arr[i-1] if i != 0 else arr[i]
            
            if prev == arr[i]:
                ans[arr[i]] = rank
            else:
                rank += 1
                ans[arr[i]] = rank
        final_arr = []
        for i in nums:
            final_arr.append(ans[i])
            
        return final_arr
            
