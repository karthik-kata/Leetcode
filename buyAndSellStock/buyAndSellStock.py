class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        difference = 0

        while r < len(prices):
            if (prices[r]<prices[l]):
                l=r
                r+=1
                continue
            difference = max( difference, prices[r] - prices[l])
            r+=1
        return(difference)
            
