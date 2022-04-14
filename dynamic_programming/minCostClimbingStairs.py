# try to minimize my cost of taking one step or two steps back
# contnually
# at step 0 or 1 just return their values
# cache result
# thanks

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache
        def dp(n):
            if n == 0:
                return cost[n]
            if n == 1:
                return cost[n]
            res = min([dp(n - 1), dp(n - 2)])
            if n > len(cost) - 1:
                return res
            else:
                return res + cost[n]
        the_cost = dp(len(cost))
        return the_cost
        
