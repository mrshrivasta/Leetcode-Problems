class Solution:
    def constructFromPrePost(self, preorder, postorder):
        pos = {v: i for i, v in enumerate(postorder)}

        def build(preL, preR, postL, postR):
            if preL > preR:
                return None

            root = TreeNode(preorder[preL])

            if preL == preR:
                return root

            left_root = preorder[preL + 1]
            idx = pos[left_root]
            left_size = idx - postL + 1

            root.left = build(
                preL + 1,
                preL + left_size,
                postL,
                idx
            )

            root.right = build(
                preL + left_size + 1,
                preR,
                idx + 1,
                postR - 1
            )

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)