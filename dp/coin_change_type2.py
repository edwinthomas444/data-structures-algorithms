'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        
        n = len(coins)

        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, amount+1):
                # exclude current coin
                # check for upto previous set of coins (i-1)
                dp[i][j] = dp[i-1][j]

                # include current coin
                if j-coins[i-1]>=0:
                    dp[i][j]+= dp[i][j-coins[i-1]]
        
        return dp[n][amount]
