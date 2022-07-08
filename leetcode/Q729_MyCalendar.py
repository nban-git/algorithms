import bisect


class MyCalendar:

    def __init__(self):
        self.booking = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect(self.booking, start, key=lambda x: x[0])
        if idx > 0:
            if self.booking[idx-1][1] > start:
                return False
        if idx < len(self.booking):
            if self.booking[idx][0] < end:
                return False
        self.booking.insert(idx, [start, end])
        return True


if __name__ == '__main__':
    obj = MyCalendar()
    assert obj.book(10, 20)
    assert not obj.book(15, 25)
    assert obj.book(30, 40)
    assert obj.book(20, 30)

    obj = MyCalendar()
    assert obj.book(37, 50)
    assert not obj.book(33, 50)
    assert obj.book(4, 17)
    assert not obj.book(35, 48)
    assert not obj.book(8, 25)