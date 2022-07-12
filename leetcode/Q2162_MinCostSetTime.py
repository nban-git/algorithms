class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, ts: int) -> int:
        # 0 <= startAt <= 9
        # 1 <= moveCost, pushCost <= 105
        # 1 <= targetSeconds <= 6039
        minCost = float("inf")
        prev = startAt
        if ts < 99:
            cost = 0
            timearr = []
            if ts > 9:
                timearr.append(ts // 10)
            timearr.append(ts % 10)
            # cost += pushCost if curr == prev else moveCost + pushCost
            # minCost = min(minCost, cost)
        else:
            m = ts // 60
            s = ts % 60
        return minCost


if __name__ == '__main__':
    sol = Solution()
    assert sol.minCostSetTime(startAt=1, moveCost=2, pushCost=1, targetSeconds=600) == 6
    assert sol.minCostSetTime(startAt=0, moveCost=1, pushCost=2, targetSeconds=76) == 6
