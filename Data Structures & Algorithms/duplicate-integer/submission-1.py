class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for j in nums:
            if j in seen:
                return True 
            seen.add(j)
        return False
        