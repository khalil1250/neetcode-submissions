class Solution:
    import math
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dynamic(n):
            if n <=1 : return 1
            if n in memo : return memo[n]
            memo[n] = dynamic(n-1) + dynamic(n-2)
            return memo[n]
        return dynamic(n) 
