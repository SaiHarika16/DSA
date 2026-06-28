class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freqs=Counter(nums)
        poss_start=[]
        curr_count=0
        res=1
        ones=freqs.get(1,0)
        if ones%2==0:
            ones-=1
        res=max(res,ones)
        for num,freq in freqs.items():
            if num!=1 and freq>=2:
                poss_start.append(num)
        for i in poss_start:
            curr=i
            while True:
                if curr not in freqs:
                    curr_count-=1
                    break
                if freqs[curr]>=2:
                    curr_count+=2
                    curr=curr**2
                elif freqs[curr]==1:
                    curr_count+=1
                    break
            res=max(res,curr_count)
            curr_count=0
        return res