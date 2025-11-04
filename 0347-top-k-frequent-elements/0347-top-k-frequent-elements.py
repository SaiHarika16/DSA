class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        res=[]
        while k:
            max_key=max(c,key=lambda num:c[num])
            res.append(max_key)
            c.pop(max_key)
            k-=1
        return res

        