class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total_sum = sum(matchsticks)
        
        # Quick check: A square must have 4 equal integer sides
        if total_sum % 4 != 0:
            return False
            
        target = total_sum // 4
        
        # Optimization 1: Sort in descending order to handle larger sticks first
        matchsticks.sort(reverse=True)
        
        # Optimization 2: If a single stick is longer than the target side, it's impossible
        if matchsticks[0] > target:
            return False
            
        # Array to track the current length of the 4 sides of the square
        sides = [0] * 4
        
        def backtrack(index: int) -> bool:
            # If all matchsticks are successfully placed
            if index == len(matchsticks):
                return True
                
            for i in range(4):
                # Check if the current stick can fit into side `i`
                if sides[i] + matchsticks[index] <= target:
                    sides[i] += matchsticks[index]
                    
                    if backtrack(index + 1):
                        return True
                        
                    # Backtrack
                    sides[i] -= matchsticks[index]
                
                # Optimization 3: If this side is empty and placing the stick here 
                # didn't lead to a solution, it won't work in any subsequent empty side either.
                if sides[i] == 0:
                    break
                    
            return False

        return backtrack(0)