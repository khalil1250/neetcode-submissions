class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left = 0
        right = len(heights)-1
        while(left<right):
            width = right - left
            res = max(res, width*min(heights[left], heights[right]))
            if(heights[left]<heights[right]):
                limit = heights[left]
                while left<right and heights[left] <= limit: 
                    left+=1
            elif(heights[left]>heights[right]):
                limit = heights[right]
                while left<right and heights[right] <= limit:
                    right-=1
            else:
                left+=1
        return res
            


        