class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        arr = list(set(letters))
        arr.sort()
        si = 0
        ei = len(arr)-1
        
        while si <= ei:
            
            mi = (si + ei) // 2
            
            if arr[-1] <= target:
                return arr[0]
            
            if arr[mi] == target:
                return arr[mi+1]
        
            
            elif arr[mi] < target:
                si = mi + 1
                
            else:
                ei = mi -1
                
        return arr[si]
            
        
