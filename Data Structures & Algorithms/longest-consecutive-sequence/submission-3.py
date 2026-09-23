class Solution:
    def countChain(self, nums, start):
        curr = start
        while(curr+1 in nums):
            curr+=1
        return curr-start+1

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: 
            return 0
        nums = set(nums)
        max_length = 1
        for n in nums:
            if(n-1 not in nums and n+1 in nums):
                length = self.countChain(nums, n)
                max_length = max(length, max_length)
        return max_length
            
            
         