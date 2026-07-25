class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack, mapping = [], {}
        for num in nums2:
            while stack and stack[-1] < num:
                mapping[stack.pop()] = num
            stack.append(num)
        return [mapping.get(num, -1) for num in nums1]