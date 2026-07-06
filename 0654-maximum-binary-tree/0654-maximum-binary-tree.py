# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left > right:
                return None

            max_idx = left
            for i in range(left + 1, right + 1):
                if nums[i] > nums[max_idx]:
                    max_idx = i

            root = TreeNode(nums[max_idx])
            root.left = build(left, max_idx - 1)
            root.right = build(max_idx + 1, right)

            return root

        return build(0, len(nums) - 1)