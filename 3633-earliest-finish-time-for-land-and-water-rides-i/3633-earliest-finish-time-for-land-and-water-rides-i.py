class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float('inf')
        for ls, ld in zip(landStartTime, landDuration):
            land_end = ls + ld
            for ws, wd in zip(waterStartTime, waterDuration):
                water_end = ws + wd
                # land then water
                t1 = max(land_end, ws) + wd
                # water then land
                t2 = max(water_end, ls) + ld
                res = min(res, t1, t2)
        return res