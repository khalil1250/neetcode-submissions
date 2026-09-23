from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cum = list(accumulate(nums, mul))
        reverseCum = list(accumulate(nums[::-1], mul))[::-1]
        res = []
        for i in range(len(nums)):
            prefix = cum[i-1] if i>0 else 1
            suffix = reverseCum[i+1] if i<len(nums)-1 else 1
            res.append(prefix*suffix)
        return res
        