from typing import List


class Solution:
    # Use sweep line algorithm
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        rooms = []
        for interval in intervals:
            for i in range(len(rooms) + 1):
                if len(rooms) < i + 1:
                    rooms.append([])
                    rooms[i].append(interval)
                    break
                if interval[0] >= rooms[i][-1][1]:
                    rooms[i].append(interval)
                    break
        return len(rooms)

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts, ends = [], []
        for s, e in intervals:
            starts.append(s)
            ends.append(e)
        starts.sort()
        ends.sort()
        rooms = 0
        i = 0
        for s in starts:
            if s < ends[i]:
                rooms += 1
            else:
                i += 1
        return rooms


if __name__ == '__main__':
    sol = Solution()
    assert sol.minMeetingRooms([[0,30],[15,20],[5,10]]) == 2
    assert sol.minMeetingRooms([[7,10],[2,4]]) == 1
    #  1 10  1 < 10 +1
    #  5 20  5 < 10 +2
    # 15 30  15 > 10 -1, 15 < 30 + 1
