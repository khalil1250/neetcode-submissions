class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if(nums[0]>0 or nums[-1]<0): 
            return []
        if(nums[0] == 0 and nums[1] == 0 and nums[2] == 0):
            return [[0,0,0]]

        res = []
        for i in range(len(nums)-2):
            val = nums[i]
            if val>0:
                break
            if i>0 and val == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1
            while left<right:
                total = val + nums[left] + nums[right]
                if total > 0 :
                    right -=1
                elif total < 0 :
                    left +=1
                else:
                    res.append([val, nums[left], nums[right]])

                    right -= 1
                    left += 1
                    while(left < right and nums[left-1] == nums[left]):
                        left +=1
                    while( left<right and nums[right] == nums[right+1]):
                        right -= 1
                    

                
        return res
