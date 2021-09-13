class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq = [i*i for i in nums]
        sq.sort()
        return sq
