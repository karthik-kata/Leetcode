#WIP
class Solution:
    def maxProfit(prices) -> int:
        max_price=0
        l=0
        while(l<len(prices)):
            r=l+1
            while(r<len(prices)):
                difference= prices[r] - prices[l]
                max_price = max(difference, max_price)
                r+=1
            l+=1
        return(max_price)
            
    print(maxProfit([7,1,5,3,6,4]))