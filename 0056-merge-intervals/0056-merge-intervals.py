class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged=[intervals[0]]
        for interval in intervals[1:]:
            last=merged[-1]
            if interval[0]<=last[1]:
                last[1]=max(last[1],interval[1])
            else:
                merged.append(interval)
        return merged       
            
        