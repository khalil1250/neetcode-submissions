class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {nums[i]:i for i in range(n)}
        result = []
        for j in range(n):
            opposite = target-nums[j]
            if opposite in seen and j!=seen[opposite]:
                return sorted([seen[opposite], j])
        