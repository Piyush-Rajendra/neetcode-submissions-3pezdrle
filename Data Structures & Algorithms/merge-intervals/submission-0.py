class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        i = 0     
        lenIntervals = len(intervals)
        while i <  lenIntervals:
            start = intervals[i][0]
            end = intervals[i][1]

            while i < lenIntervals - 1 and end >= intervals[i+1][0]:
                end = max(end, intervals[i+1][1])
                i += 1
            res.append([start, end])
            i += 1
        return res
        