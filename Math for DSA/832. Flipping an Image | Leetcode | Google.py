class Solution:
#   O(n2)
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for arr in image:
            i=0
            j = len(arr)-1
            while i <= j:
                # Invert 0 and 1 ----> simultaniously flip array
                temp = 1^ (arr[i])
                arr[i]= 1^ arr[j]
                arr[j]= temp
                i += 1
                j -= 1
        return image
