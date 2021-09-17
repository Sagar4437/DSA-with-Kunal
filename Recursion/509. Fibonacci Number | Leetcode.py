class Solution:
    def fib(self, n: int) -> int:
        def fibbo(n):
            if n < 2:
                return n
            return fibbo(n-1) + fibbo(n-2)
        return fibbo(n)
