class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        max_end=intervals[0][1]
        count=1
        for interval in intervals[1:]:
            if interval[1]<=max_end:
                continue
            max_end=interval[1]
            count+=1
        return count