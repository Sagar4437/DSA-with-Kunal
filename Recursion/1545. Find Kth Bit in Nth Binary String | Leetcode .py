class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def revBit(str1):
            l = list(str1)
            for i in range(len(str1)):
                if l[i] == "0":
                    l[i] = "1"
                else:
                    l[i] = "0"

            return "".join(l[::-1])

        def bits(n):
            if n <= 1:
                return "0"

            straight_str = bits(n-1)
            reversed_str = revBit(straight_str)

            return straight_str + "1" + reversed_str
        
        return bits(n)[k-1]
        

