class Solution:
    def binaryGap(self, n: int) -> int:
        n_bin=format(n,"b")
        prev_idx=n_bin.index("1")
        res=0
        for i in range(len(n_bin)):
            if n_bin[i]=="1":
                curr_idx=i
                res=max(res,curr_idx-prev_idx)
            prev_idx=curr_idx
        return res     