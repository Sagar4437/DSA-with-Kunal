class Solution:
    '''
    here we have to sort elements between 1 - N ---> apply Cyclic sort
    '''
    def findDisappearedNumbers(self, arr: List[int]) -> List[int]:
        i = 0
        while i < len(arr):

            ci = arr[i]-1
            if arr[i] > len(arr):
                i += 1
            elif arr[ci] == arr[i]:
                i += 1
            else:
                arr[i],arr[ci] = arr[ci], arr[i]
        r = []
        for i in range(len(arr)):
            if i+1 != arr[i]:
                r.append(i+1)
        return r
