class Solution:
    def numberOfSteps(self, num: int) -> int:
      '''
      Here I have used recursion
      '''
        def fun(num,s=0):
            if num == 0:
                return 0
            
            if num%2==0:
                num /= 2
            else:
                num -= 1
                
            return 1 + fun(num)
        return fun(num)
                
