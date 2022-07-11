class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i = 0
        while i < len(start) - 1:
            if start[i] == end[i]:
                i += 1
                continue
            if (start[i:i+2] == "RX" and end[i:i+2] == "XR") or (start[i:i+2] == "XL" and end[i:i+2] == "LX"):
                i += 2
            else:
                return False
        if i < len(start):
            return start[i] == end[i]
        return True

if __name__ == '__main__':
    sol = Solution()
    assert sol.canTransform("RXXLRXRXL", "XRLXXRRLX") == True
    assert sol.canTransform("RXXLRXRXL", "RXXLRXRXL") == True
    assert sol.canTransform("RXXLRXRXL", "XRLXXRXRL") == True
    assert sol.canTransform("RXXLRXRXL", "XRLXXRRLX") == True
    assert sol.canTransform("XXXXXLXXXX", "LXXXXXXXXX") == True
    "XXXXXLXXXX"
    "LXXXXXXXXX"
    assert sol.canTransform("X", "L") == False

# RX - XR, XL -> LX
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
#                 XRLXXRRLX