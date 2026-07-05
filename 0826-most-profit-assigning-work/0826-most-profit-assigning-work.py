class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        # Step 1: Pair difficulty with profit and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        
        # Step 2: Sort workers by their ability
        worker.sort()
        
        total_profit = 0
        max_profit = 0
        job_idx = 0
        n = len(jobs)
        
        # Step 3: Iterate through each worker
        for ability in worker:
            # Advance the job pointer for all jobs this worker can handle
            while job_idx < n and jobs[job_idx][0] <= ability:
                # Keep track of the highest profit available up to this difficulty
                max_profit = max(max_profit, jobs[job_idx][1])
                job_idx += 1
            
            # Add the best possible profit for the current worker
            total_profit += max_profit
            
        return total_profit