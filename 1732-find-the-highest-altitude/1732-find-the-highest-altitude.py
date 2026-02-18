class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start=0
        res=0
        for i in gain:
            start=start+i
            res=max(res,start)
        return res
