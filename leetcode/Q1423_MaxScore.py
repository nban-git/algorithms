from typing import List


class Solution:
    def maxScore2(self, cardPoints: List[int], k: int) -> int:
        curScore, score = 0, 0
        for i in range(k):
            curScore += cardPoints[i]
        score = curScore

        n = len(cardPoints)
        if k < n:
            l, r = k, len(cardPoints)
            while l > 0:
                l -= 1
                r -= 1
                curScore = curScore - cardPoints[l] + cardPoints[r]
                score = max(score, curScore)
        return score

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        minSum = float("inf")
        start, curSum = 0, 0
        for i in range(len(cardPoints)):
            if i - start >= size:
                minSum = min(minSum, curSum)
                curSum -= cardPoints[start]
                start += 1
            curSum += cardPoints[i]
        return sum(cardPoints) - minSum


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxScore([1,2,3,4,5,6,1], 3) == 12
    assert sol.maxScore([1,2,3,4,5,6,1], 5) == 19
    assert sol.maxScore([2,2,2], 2) == 4
    assert sol.maxScore([9,7,7,9,7,7,9], 7) == 55
    assert sol.maxScore([100,40,17,9,73,75], 3) == 248
