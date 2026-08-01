class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # stores complete word at terminal node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        m, n = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return

            next_node = node.children[char]

            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # deduplicate — don't find same word twice

            board[r][c] = "#"  # mark visited

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)

            board[r][c] = char  # restore

            # Prune exhausted trie branches
            if not next_node.children:
                del node.children[char]

        for r in range(m):
            for c in range(n):
                dfs(r, c, root)

        return result