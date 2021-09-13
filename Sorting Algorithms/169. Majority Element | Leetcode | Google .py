class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = 0
        
        for i in nums:
            if d[i] == 0:
                d[i] = 1
            else:
                d[i] += 1
        d1 = {}
        for k,v in d.items():
            d1[v] = k
            
        return d1[max(d1.keys())]
        
