# 17.1 COMPUTE AN OPTIMUM ASSIGNMENT OF TASKS

# Design an algorithm that takes as input a set of tasks and returns an optimum
# assignment.
# Hint: What additional task should be assigned to the worker who is assigned
# the longest task?

from typing import List
import collections
PairedTasks = collections.namedtuple('PairedTask',('task1','task2'))

class Solution:
    # Time complexity is O(nLog(n)) dominated by the sort method
    # Space is O(n)
    def assign_tasks(self,task_durations:List)->List[PairedTasks]:
        # sort
        task_durations.sort()
        tasks = []
        # end to end go
        for i in range(len(task_durations)//2):
            tasks.append(PairedTasks(task_durations[i],task_durations[-i]))
        return tasks

if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.assign_tasks([1,2,3,4,5,6]))
