# https://neetcode.io/problems/task-scheduling

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounter=Counter(tasks)
        maxHeap=[-cnt for cnt in taskCounter.values()]
        heapq.heapify(maxHeap)
        time=0
        q=deque()
        while maxHeap or q:
            time+=1
            if maxHeap:
                cnt=1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time+n])
            if q and time==q[0][1]:
                
                heapq.heappush(maxHeap ,q.popleft()[0])

        return time


