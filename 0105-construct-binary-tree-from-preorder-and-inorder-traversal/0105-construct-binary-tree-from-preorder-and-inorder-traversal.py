class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}
        pre = iter(preorder)
        def build(lo, hi):
            if lo > hi: return None
            val = next(pre)
            mid = idx[val]
            node = TreeNode(val)
            node.left = build(lo, mid-1)
            node.right = build(mid+1, hi)
            return node
        return build(0, len(inorder)-1)