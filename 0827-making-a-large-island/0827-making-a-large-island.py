class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        island_sizes = {0: 0} # Maps island_id -> size. 0 represents water (size 0)
        island_id = 2        # Start IDs from 2 to avoid collision with 0 and 1
        
        # Helper function to perform DFS and label the entire island
        def dfs(r, c, curr_id):
            if not (0 <= r < n and 0 <= c < n) or grid[r][c] != 1:
                return 0
            grid[r][c] = curr_id
            size = 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                size += dfs(r + dr, c + dc, curr_id)
            return size

        # Step 1: Label all existing islands and store their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = dfs(r, c, island_id)
                    island_sizes[island_id] = size
                    island_id += 1
                    
        # If there are no water cells, the max island size is the total grid size
        max_island = max(island_sizes.values(), default=0)
        
        # Step 2: Try converting every 0 to a 1 and calculate combined size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen_islands = set()
                    # Check all 4 cardinal neighbors
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen_islands.add(grid[nr][nc])
                    
                    # Size of new island is 1 (the flipped cell) + sizes of unique adjacent islands
                    current_possible_size = 1 + sum(island_sizes[id] for id in seen_islands)
                    max_island = max(max_island, current_possible_size)
                    
        return max_island