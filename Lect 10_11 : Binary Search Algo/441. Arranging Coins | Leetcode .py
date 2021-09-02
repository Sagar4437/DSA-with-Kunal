class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = n
        for i in range(n+1):
            if ans - i < 0:
                return i-1
            ans -= i
        return 1
            
