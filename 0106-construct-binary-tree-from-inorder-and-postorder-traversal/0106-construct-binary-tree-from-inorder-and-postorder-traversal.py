class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}
        post = iter(reversed(postorder))
        def build(lo, hi):
            if lo > hi: return None
            val = next(post)
            mid = idx[val]
            node = TreeNode(val)
            node.right = build(mid+1, hi)
            node.left = build(lo, mid-1)
            return node
        return build(0, len(inorder)-1)