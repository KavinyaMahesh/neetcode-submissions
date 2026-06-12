class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof=float('-inf')
        min_num=float('inf')
        profit=0
        

        for num in prices:
            if num<min_num:
                min_num=num
            profit=num-min_num
            
            max_prof=max(max_prof, profit) 

        return max_prof

        