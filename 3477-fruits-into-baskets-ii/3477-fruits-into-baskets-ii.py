class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        occupied=[False]*len(fruits)
        res=0
        for fruit in fruits:
            placed=False
            for i in range(len(baskets)):
                if(not occupied[i] and baskets[i]>=fruit):
                    placed=True
                    occupied[i]=True
                    break
            if not placed:
                res+=1
        return res
