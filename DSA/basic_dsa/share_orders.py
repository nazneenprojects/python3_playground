"""
Buying and selling shares – maximum one transaction

Given an array prices[] of length N representing the stock prices on different days.
The task is to achieve the highest possible profit by buying and selling the stocks on different days when at most
one transaction is allowed. Here, a transaction means 1 purchase + 1 sale.

Note: Shares must be purchased before selling

Input: Prices[] = {7, 10, 1, 3, 6, 9, 2}
Output: 8
Explanation: Buy at price 1 and sell at price 9.


Input: Prices[] = {7, 6, 4, 3, 1}
Output: 0
Explanation:   Since the array is sorted in descending order, a profit of 0 can be made without any transaction.

Input: Prices[] = {1, 3, 6, 9, 11}
Output: 10
Explanation:   Since the array is sorted in ascending order, we can get the maximum profit by buying at price[0]
and selling at price[n-1].

"""


def share_order(prices):
    print("share purchase:")
    res = 0
    n = len(prices)

    for i in range(n-1):

        for j in range(i+1, n):
           # print("res:", res)
            res = max(res, prices[i] - prices[j])
            # print( prices[i] , "---and--",  prices[j], "   diff: ",prices[i] - prices[j], "res:",prices[i] - prices[j])

    #print(res)

if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    share_order(prices)
