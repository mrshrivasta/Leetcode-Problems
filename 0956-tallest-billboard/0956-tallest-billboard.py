class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}  # diff -> taller height

        for rod in rods:
            curr = dp.copy()

            for diff, taller in curr.items():
                # add rod to taller side
                dp[diff + rod] = max(dp.get(diff + rod, 0), taller + rod)

                # add rod to shorter side
                new_diff = abs(diff - rod)
                new_taller = taller + max(0, rod - diff)
                dp[new_diff] = max(dp.get(new_diff, 0), new_taller)

        return dp[0]