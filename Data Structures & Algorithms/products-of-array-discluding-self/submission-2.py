from numpy import cumprod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cum = list(cumprod(nums))
        reverseCum = list(cumprod(nums[::-1]))[::-1]
        print(len(nums),len(cum),len(reverseCum))
        res = []
        for i, n in enumerate(nums):
            prefix = cum[i-1] if i>0 else 1
            suffix = reverseCum[i+1] if i<len(nums)-1 else 1
            res.append(prefix*suffix)
        return res
            


        