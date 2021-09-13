class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [i for i in nums if i%2 == 0]
        odd = [i for i in nums if i%2 != 0]
        
        final = []
        ii = 0
        i = 0
        j = 0
        while ii < (len(even)+len(odd)):
            if ii%2 == 0:
                final.append(even[i])
                i += 1
            else:
                final.append(odd[j])
                j += 1
            ii += 1
        return final
