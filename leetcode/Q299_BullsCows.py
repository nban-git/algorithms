from collections import defaultdict


class Solution:
    def getHint2(self, secret: str, guess: str) -> str:
        sCount, gCount = defaultdict(int), defaultdict(int)
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                sCount[secret[i]] += 1
                gCount[guess[i]] += 1
        cows = 0
        for n in sCount.keys():
            if n in gCount.keys():
                cows += min(sCount[n], gCount[n])
        return "{}A{}B".format(bulls, cows)

    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        count = [0 for i in range(10)]
        for i in range(len(secret)):
            s = int(secret[i])
            g = int(guess[i])
            if s == g:
                bulls += 1
            else:
                if count[s] > 0: cows += 1
                if count[g] < 0: cows += 1
                count[s] += 1
                count[g] -= 1
        return "{}A{}B".format(bulls, cows)

if __name__ == '__main__':
    sol = Solution()
    assert sol.getHint("1807", "7810") == "1A3B"
    assert sol.getHint("1123", "0111") == "1A1B"