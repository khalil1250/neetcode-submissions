class Solution:
    def binarySearch(self, nums: List[int], target: int, l, r):
        while l<=r: 
            m = (l+r)//2
            mval = nums[m]
            print(l, m, r)
            if mval == target:
                return m
            if mval < target:
                l = m + 1
            else:
                r = m - 1
        return -1 
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        split = nums[0] 
        idx = 0
        while l<=r: 
            if nums[l]<= nums[r]:
                split = min(split, nums[l])
                idx = l if split == nums[l] else idx
                break
            m = (l+r)//2
            if nums[l] <= nums[m]: 
                split = min(nums[l], split)
                idx = l if split == nums[l] else idx
                l = m+1
            else: 
                split = min(nums[m], split)
                idx = m if split == nums[m] else idx
                r = m-1
        
        first = self.binarySearch(nums, target, idx, len(nums)-1)
        if first != -1 :
            return first
        second = self.binarySearch(nums, target, 0, idx)
        return second
            