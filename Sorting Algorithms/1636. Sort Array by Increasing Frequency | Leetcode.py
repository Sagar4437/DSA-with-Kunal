class Solution:
    def frequencySort(self, arr: List[int]) -> List[int]:
        arr.sort(reverse=True)
        return sorted(arr, key = lambda x: arr.count(x))
