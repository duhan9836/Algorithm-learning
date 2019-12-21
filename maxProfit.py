import random
def maxProfit(prices):
    """
    :type prices: List[int] with at least 2 items
    :rtype: int
    """
    buyprice = prices[0]
    i = 1
    profit = 0
    while i in range(1, len(prices)):
        if prices[i] >= prices[i - 1]:  # when price keeps going up, hold the position,ie the same buyprice.
            i += 1
        else:  # when price goes down, sell with the previous price
            sellprice = prices[i - 1]
            profit = profit + (sellprice - buyprice)  # calculate profit
            buyprice = prices[i]  # reset the buyprice
            i += 1
    if buyprice != prices[-1]:
        profit = profit + (prices[-1] - buyprice)  # thus hold till end to sell would be the best choice.
    return profit

a=[7,1,5,3,6,4,10,3,9,8,2,6]
print(maxProfit(a))

b=[random.randrange(20) for i in range(20)]

print(b,maxProfit(b))