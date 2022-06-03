import bisect
from typing import List


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        painted = []
        result = []
        for x, y in paint:
            distance = y - x
            if len(painted) > 0:
            #     result.append(y - x)
            # else:
                start = bisect.bisect_left(painted, x, key=lambda i: i[0])
                end = bisect.bisect_right(painted, y, key=lambda i: i[1])
                distance = y - x
                print("x={}, y={}, start={}, end={}, distance={}, painted={}".format(x, y, start, end, distance, painted))
                for i in range(start, min(end+1, len(painted))):
                    if x > painted[i][0]:
                        if y > painted[i][1]:
                            distance -= painted[i][1] - painted[i][0]
                        else:
                            distance -= y - painted[i][0]
                    else:
                        distance -= painted[i][0] - x
                if start == len(painted):
                    if painted[start - 1][1] > x:
                        distance -= painted[start - 1][1] - x

            result.append(distance)
            painted.append([x, y])
            painted.sort()
            print("\tafter appending new coord={}, painted={}".format((x,y), painted))
            temp = []
            last = painted[0]
            for i in range(1, len(painted)):
                if last[1] >= painted[i][0]:
                    last[1] = painted[i][1]
                else:
                    temp.append(last)
                    last = painted[i]
            temp.append(last)
            print("\t** temp={}".format(temp))
            painted = temp
        print("result={}".format(result))
        return result


if __name__ == '__main__':
    sol = Solution()
    # assert sol.amountPainted([[1, 4], [4, 7], [5, 8]]) == [3, 3, 1]
    # assert sol.amountPainted([[1, 4], [5, 8], [4, 7]]) == [3, 3, 1]
    assert sol.amountPainted([[1, 5], [2, 4]]) == [4, 0]
    assert sol.amountPainted([[3, 5], [1, 3], [4, 5], [3, 4]]) == [2, 2, 0, 0]
    assert sol.amountPainted([[0, 5], [0, 2], [0, 3], [0, 4], [0, 5]]) == [5, 0, 0, 0, 0]
