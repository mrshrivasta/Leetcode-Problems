class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(index, path):
            if len(path) >= 2:
                res.append(list(path))
            
            used = set()
            for i in range(index, len(nums)):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
                    
        backtrack(0, [])
        return res