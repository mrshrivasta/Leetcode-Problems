class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict, deque
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1/v
        
        def bfs(src, dst):
            if src not in graph or dst not in graph: return -1.0
            if src == dst: return 1.0
            visited = set()
            q = deque([(src, 1.0)])
            while q:
                node, prod = q.popleft()
                if node == dst: return prod
                visited.add(node)
                for nei, val in graph[node].items():
                    if nei not in visited:
                        q.append((nei, prod*val))
            return -1.0
        
        return [bfs(c, d) for c, d in queries]