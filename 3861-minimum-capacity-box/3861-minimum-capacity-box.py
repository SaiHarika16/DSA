class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        min_caps=float("inf")
        res_ind=-1
        for i in range(len(capacity)):
            if capacity[i]>=itemSize and capacity[i]<min_caps:
                    min_caps=capacity[i]
                    res_ind=i
        return res_ind