class Solution:
    def productExcept(self, nums, index):
        res = 1
        for i, n in enumerate(nums):
            if(i != index):
                res *= n
        return res 

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for n in nums:
            product *= n
        res = [int(product/n) if n != 0 else self.productExcept(nums, i) for i, n in enumerate(nums)]
        return res

        