class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        width=0
        maxWidth=0
        while left<right:
            width=right-left
            if heights[left]<heights[right]:
                curr=heights[left]
                left+=1
            else:
                curr=heights[right]
                right-=1
            currVol=curr*width
            maxWidth=max(maxWidth,currVol)
        return maxWidth