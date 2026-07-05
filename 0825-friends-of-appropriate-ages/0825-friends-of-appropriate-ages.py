from collections import Counter

class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        # Count the frequency of each age
        age_counts = Counter(ages)
        total_requests = 0
        
        # Iterate over all possible pairs of unique ages
        for age_x, count_x in age_counts.items():
            for age_y, count_y in age_counts.items():
                
                # Check if age_x can send a request to age_y
                if age_y <= 0.5 * age_x + 7:
                    continue
                if age_y > age_x:
                    continue
                
                # If valid, calculate the number of requests sent
                if age_x == age_y:
                    # A person cannot request themselves, so subtract 1 from options
                    total_requests += count_x * (count_x - 1)
                else:
                    # Every person of age_x requests every person of age_y
                    total_requests += count_x * count_y
                    
        return total_requests