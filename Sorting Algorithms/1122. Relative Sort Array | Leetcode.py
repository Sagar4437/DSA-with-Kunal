class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = []
        for i in arr2:
            val = arr1.count(i)
            for j in range(val):
                arr.append(i)
                arr1.pop(arr1.index(i))
                
        arr1.sort()
        arr.extend(arr1)
        return arr
                
