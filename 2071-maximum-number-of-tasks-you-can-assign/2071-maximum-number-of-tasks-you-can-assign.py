from bisect import bisect_left
from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def can_assign(mid):
            pills_used = 0
            best_workers = SortedList(workers[-mid:])  # top `mid` strongest workers

            for i in reversed(range(mid)):  # hardest to easiest tasks
                req = tasks[i]
                if best_workers[-1] >= req:
                    best_workers.pop()  # assign directly
                elif pills_used < pills:
                    idx = best_workers.bisect_left(req - strength)
                    if idx == len(best_workers):
                        return False
                    best_workers.pop(idx)
                    pills_used += 1
                else:
                    return False
            return True

        left, right = 0, min(len(tasks), len(workers))
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
