class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_v = 0
        volume = 0
        pointer1 = 0
        pointer2 = len(height) - 1
        while pointer1 < pointer2:
            volume = min(height[pointer1],height[pointer2]) * (pointer2 - pointer1)
            if volume > max_v:
                max_v = volume
            if height[pointer1] < height[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1
        return(max_v)