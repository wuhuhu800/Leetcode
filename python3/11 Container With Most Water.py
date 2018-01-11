'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

'''
#此题是复杂度题
class Solution: #遍历一次
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s_low =0
        s_high = len(height)-1
        s_all=[]
        while s_low < s_high:
            s_width = s_high-s_low
            s_leigth = min(height[s_low],height[s_high])
            s_area = s_width*s_leigth
            if height[s_low] < height[s_high]:
                s_low  +=1
            else:
                s_high -=1
            s_all.append(s_area)
        return max(s_all)
