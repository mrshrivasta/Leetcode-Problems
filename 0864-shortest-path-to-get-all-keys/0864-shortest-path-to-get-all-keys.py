from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        
        start_r, start_c = 0, 0
        total_keys = 0
        
        # Step 1: Find the starting position and count total number of keys
        for r in range(m):
            for c in range(n):
                cell = grid[r][c]
                if cell == '@':
                    start_r, start_c = r, c
                elif 'a' <= cell <= 'f':
                    total_keys += 1
                    
        # The target mask when all keys are collected
        # e.g., if total_keys = 3, target = (1 << 3) - 1 = 7 (binary: 111)
        target_mask = (1 << total_keys) - 1
        
        # Queue stores tuples of: (row, col, current_key_mask, distance)
        queue = deque([(start_r, start_c, 0, 0)])
        
        # Visited set tracks: (row, col, current_key_mask)
        visited = {(start_r, start_c, 0)}
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Step 2: Standard BFS
        while queue:
            r, c, mask, dist = queue.popleft()
            
            # If we've collected all keys, return the distance immediately
            if mask == target_mask:
                return dist
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundary conditions and walls
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != '#':
                    cell = grid[nr][nc]
                    next_mask = mask
                    
                    # Case 1: Encountered a Key
                    if 'a' <= cell <= 'f':
                        # Update bitmask to include this key
                        key_bit = ord(cell) - ord('a')
                        next_mask |= (1 << key_bit)
                        
                    # Case 2: Encountered a Lock
                    elif 'A' <= cell <= 'F':
                        # Check if we have the matching key
                        lock_bit = ord(cell) - ord('A')
                        if not (mask & (1 << lock_bit)):
                            continue  # Can't pass without the key
                            
                    # Case 3: Empty cell '.' or Start cell '@' (can be freely crossed)
                    
                    # If this state (nr, nc, next_mask) hasn't been visited yet, queue it
                    if (nr, nc, next_mask) not in visited:
                        visited.add((nr, nc, next_mask))
                        queue.append((nr, nc, next_mask, dist + 1))
                        
        return -1