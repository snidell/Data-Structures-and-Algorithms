
from typing import List
import copy
class SnapShot():
    def __init__(self,length):
        self.snap_id = -1
        self.data = {}
        self.snapshot_map = {}

    # void set(index, val) sets the element at the given index to be equal to val.
    def set(self,index,val)-> None:
        self.data[index] = val

    # int snap() takes a snapshot of the array and returns the snap_id:
    # the total number of times we called snap() minus 1.
    def snap(self)-> int:
        self.snap_id += 1
        self.snapshot_map[self.snap_id] = self.data.copy()
        return self.snap_id
    # int get(index, snap_id) returns the value at the given index, at the
    # time we took the snapshot with the given snap_id
    def get(self,index,snap_id)-> int:
        if snap_id in self.snapshot_map and index in self.snapshot_map[snap_id]:
            return self.snapshot_map[snap_id][index]
        return 0



if __name__ =="__main__":
    mySnapShot = SnapShot(3)
    mySnapShot.set(0,5)
    print(mySnapShot.snap())
    mySnapShot.set(0,6)
    print(mySnapShot.get(0,0))
