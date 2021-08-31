'''
Approch :
3 Steps:
1) find peak element index
2) Apply binary search on assending array having range 0 to peak
		# This will return 1st occurance in assending arr
3) Apply binary search on decending array having range peak+1 to len(arr) -1
		# This will return 1st occurance in decending arr
		
retrun 1st occ index


'''


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    #search will return index of peak element
    def search(self,arr):
        si = 0
        ei = arr.length() - 1
        
        while si != ei:
            mi = (si + ei) // 2
            if arr.get(mi) > arr.get(mi+1):
                ei = mi
            else:
                si = mi + 1
        return si
    
    def binary1(self,arr,target,si,ei):
        while si <= ei:
            mi = (si + ei) // 2
            if arr.get(mi) == target:
                return mi
            
            elif arr.get(mi) < target:
                si = mi + 1
            
            else:
                ei = mi - 1
                
        return -1
    
    def binary2(self,arr,target,si,ei):
        while si <= ei:
            mi = (si + ei) // 2
            if arr.get(mi) == target:
                return mi
            
            elif arr.get(mi) > target:
                si = mi + 1
            
            else:
                ei = mi - 1
                
        return -1
    
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        
        peak = self.search(arr)
        i = self.binary1(arr,target,0,peak)
        j = self.binary2(arr,target,peak+1,arr.length()-1)
        
        if i != -1:
            return i
        else:
            return j
        
        
