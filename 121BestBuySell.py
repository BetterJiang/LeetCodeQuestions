# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:55:55 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

121. Best Time to Buy and Sell Stock

Input: [7,1,5,3,6,4]
Output: 5
Explanation:
    Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""


def maxProfit2(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


def maxProfit(prices):
    vmin = 10000000
    pmax = 0
    for el in prices:
        if el < vmin:
            vmin = el
        elif el - vmin > pmax:
            pmax = el - vmin
    return pmax




prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]




class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """




#public class Solution {
#    public int maxProfit(int prices[]) {
#        int minprice = Integer.MAX_VALUE;
#        int maxprofit = 0;
#        for (int i = 0; i < prices.length; i++) {
#            if (prices[i] < minprice)
#                minprice = prices[i];
#            else if (prices[i] - minprice > maxprofit)
#                maxprofit = prices[i] - minprice;
#        }
#        return maxprofit;
#    }
#}