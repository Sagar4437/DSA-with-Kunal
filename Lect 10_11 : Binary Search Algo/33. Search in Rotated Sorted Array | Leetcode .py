class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if target not in arr:
            return -1
        return arr.index(target)
        
