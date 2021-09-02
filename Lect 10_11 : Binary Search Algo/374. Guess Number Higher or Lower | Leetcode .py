# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        si = 1
        ei = n

        while (si <= n) and (ei > 0):
            pick = (si + ei) // 2
            num = guess(int(pick))

            if num == 1:
                si = pick+1
            elif num == -1:
                ei = pick-1
            elif num == 0:
                return pick
            
        return n
