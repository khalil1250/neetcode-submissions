class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def robDP(i, nums):
            if i >= len(nums) : return 0
            if i in memo: return memo[i]
            leave_i = robDP(i+1, nums)
            steal_i = robDP(i+2, nums)+nums[i]
            memo[i] = max(steal_i, leave_i) 
            return memo[i]
        return robDP(0, nums)
