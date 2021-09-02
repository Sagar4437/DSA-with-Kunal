class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        c = 0
        ans = 0
        i = 0
        while c < k:
            i += 1
            if i not in arr:
                c += 1
                ans = i
        return ans
