class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Preorder traversal — uniquely determines BST structure
        vals = []
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ','.join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals = deque(int(x) for x in data.split(','))

        def build(min_val, max_val):
            if not vals or vals[0] < min_val or vals[0] > max_val:
                return None
            val = vals.popleft()
            node = TreeNode(val)
            node.left  = build(min_val, val)
            node.right = build(val, max_val)
            return node

        return build(float('-inf'), float('inf'))