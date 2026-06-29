class Solution:
    def trap(self, height: List[int]) -> int:
        left, right   = 0, len(height) - 1
        max_left      = max_right = 0
        water         = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]      # new left max, no water here
                else:
                    water += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]    # new right max, no water here
                else:
                    water += max_right - height[right]
                right -= 1

        return water