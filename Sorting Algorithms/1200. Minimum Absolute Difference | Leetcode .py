class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        '''
        O(n)
        '''
        MAX = 99999999999
        arr.sort()
        l = []
        for i in range(1,len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < MAX:
                l.clear() 
                MAX = diff
                l.append([arr[i-1],arr[i]])
            elif diff == MAX:
                l.append([arr[i-1],arr[i]])
        
        
        return(l)
