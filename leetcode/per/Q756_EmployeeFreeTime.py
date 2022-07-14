"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
import bisect


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

# 1 <= schedule.length , schedule[i].length <= 50
# 0 <= schedule[i].start < schedule[i].end <= 10^8

class Solution:
    def employeeFreeTime2(self, schedule: '[[Interval]]') -> '[Interval]':
        working = []
        for emp in schedule:
            for s in emp:
                start = bisect.bisect_left(working, s.start)
                end = bisect.bisect_right(working, s.end)

                slots = []
                if start % 2 == 0:
                    slots.append(s.start)
                if end % 2 == 0:
                    slots.append(s.end)
                working[start:end] = slots

        result = list()
        for i in range(2, len(working), 2):
            result.append(Interval(working[i-1], working[i]))

        for i in result:
            print(i.start, i.end)
        return result

    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted([it for emp in schedule for it in emp], key=lambda x: x.start)
        result = []
        pre = intervals[0]
        for it in intervals[1:]:
            if it.start <= pre.end < it.end:
                pre.end = it.end
            elif it.start > pre.end:
                result.append(Interval(pre.end, it.start))
                pre = it
        return result


if __name__ == '__main__':
    sol = Solution()
    sol.employeeFreeTime([[Interval(1,2),Interval(5,6)],[Interval(1,3)],[Interval(4,10)]])
    sol.employeeFreeTime([[Interval(1,3),Interval(6,7)],[Interval(2,4)],[Interval(2,5),Interval(9,12)]])