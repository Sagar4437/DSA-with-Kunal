# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        si = 1
        ei = n
        

        while si <= ei:
            mi = (si + ei) // 2
                        
            if isBadVersion(1) :
                return 1
            
            elif not isBadVersion(mi) and isBadVersion(mi+1):
                return mi+1
            
            elif isBadVersion(mi):
                ei = mi - 1
                
            else:
                si = mi + 1
                
        
