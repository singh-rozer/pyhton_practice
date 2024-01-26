#Approach 1: Brute
#TC = O(n) SC = O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=1
        r=1
        dicts=0
        for i,j in enumerate(prices):
            l=min(l,j)
            if l == j:
                dicts = i
        for k in range(dicts,len(prices)):
            r = max(r,prices[k])
        return r-l

#Approach 2: Two pointer
#TC = O(n) SC = O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,pr=0,1,0
        while r<len(prices):
            diff = prices[r]-prices[l]
            if prices[r] > prices[l]:
                pr = max(pr,diff)
            else:
                l=r
            r+=1
        return pr
