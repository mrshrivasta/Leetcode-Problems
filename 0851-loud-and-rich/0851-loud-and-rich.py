class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        n = len(quiet)
        
        # Step 1: Construct the graph (poorer -> richer)
        graph = [[] for _ in range(n)]
        for a, b in richer:
            graph[b].append(a)
            
        # res[i] will store the identity of the quietest person 
        # among those equal to or richer than person i.
        res = [-1] * n
        
        # Step 2: Define the DFS with memoization
        def dfs(node):
            # If already calculated, return the cached answer
            if res[node] != -1:
                return res[node]
            
            # Base case: The person themselves is the initial candidate
            quietest_person = node
            
            # Explore all people who are directly richer than 'node'
            for richer_person in graph[node]:
                # Find the quietest person reachable through this richer path
                candidate = dfs(richer_person)
                
                # Update if the candidate's quietness is lower
                if quiet[candidate] < quiet[quietest_person]:
                    quietest_person = candidate
                    
            # Memoize the result
            res[node] = quietest_person
            return res[node]
        
        # Step 3: Run DFS for every person to fill out the array
        for i in range(n):
            dfs(i)
            
        return res