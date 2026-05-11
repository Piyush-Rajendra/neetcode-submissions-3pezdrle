class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # handle k can it be greater than > point[n]
        # soln: calculate distance of each point and sort it calc : constant time and space O(n) and sort them
        # nlogn so time will be O(nlogn) amd space will be o(n) and return first k so its just O(n)
        # points.sort(key = lambda p: p[0]**2 + p[1] **2)
        # return points[:k]
        # min heap k log n O(n)
        
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1

        return res