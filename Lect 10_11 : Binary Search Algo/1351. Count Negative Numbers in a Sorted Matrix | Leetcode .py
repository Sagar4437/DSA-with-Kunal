class Solution:
    
    def findNegIndex(self,arr):
        si = 0
        ei = len(arr) -1
        ans = -1
        while si <= ei:
            mi = (si + ei) // 2
            
            if arr[mi] < 0:
                ans = mi
                ei = mi - 1
            else:
                si = mi + 1
                
        return ans
            
    
    
    def countNegatives(self, grid: List[List[int]]) -> int:
    
        # [  4 , 3 ,  2 , -1 ]
        # [  3 , 2 ,  1 , -1 ]
        # [  1 , 1 , -1 , -2 ]
        # [ -1 ,-1 , -2 , -3 ]
        
        c = 0
        for arr in grid:
            idx = self.findNegIndex(arr)
            if idx != -1:
                c += len(arr) - idx
            
        return c
        
        
