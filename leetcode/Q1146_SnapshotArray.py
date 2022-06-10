from bisect import bisect_left
from typing import Any, List


class SnapshotArray:
    def __init__(self, length: int):
        self.store = [[[-1,0]] for _ in range(length)]
        self.snapCount = 0

    def set(self, index: int, val: int) -> None:
        self.store[index].append([self.snapCount, val])

    def snap(self) -> int:
        self.snapCount += 1
        return self.snapCount - 1

    def get(self, index: int, snap_id: int) -> int:
        k = bisect_left(self.store[index], snap_id+1, key=lambda i: i[0]) - 1
        return self.store[index][k][1]

# i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
#         return self.A[index][i][1]
def callback(fname: str, obj: Any, args: List) -> Any:
    if fname == "SnapshotArray":
        return SnapshotArray(args[0])
    elif fname == "set":
        obj.set(args[0], args[1])
    elif fname == "get":
        return obj.get(args[0], args[1])
    elif fname == "snap":
        obj.snap()


if __name__ == '__main__':
    # fnames = ["SnapshotArray","set","snap","set","get"]
    # params = [[3],[0,5],[],[0,6],[0,0]]
    # # result = [null,null,0,null,5]

    fnames = ["SnapshotArray", "set", "set", "set", "snap", "get", "snap"]
    params = [[1], [0, 4], [0, 16], [0, 13], [], [0, 0], []]
    # output = [null,null,null,null,0,13,1]

    fnames = ["SnapshotArray", "snap", "snap", "get", "set", "snap", "set"]
    params = [[4], [], [], [3, 1], [2, 4], [], [1, 4]]

    result = []
    obj = callback(fnames[0], None, params[0])
    result.append(obj)
    for i in range(1, len(fnames)):
        result.append(callback(fnames[i], obj, params[i]))

    print(result)
