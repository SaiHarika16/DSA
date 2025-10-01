class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full_botts=numBottles
        empty_botts=full_botts
        while empty_botts>=numExchange:
            curr_full=empty_botts//numExchange
            full_botts+=curr_full
            empty_botts=curr_full+(empty_botts%numExchange)
        return full_botts