"""
https://leetcode.com/problems/gas-station/description/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days&status=TO_DO&difficulty=MEDIUM%2CHARD
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        if sum(gas)<sum(cost):
            return -1

        totalGas=0
        currGas=0
        start=0
        
        for i in range(n):
            totalGas+=gas[i]-cost[i]
            currGas+=gas[i]-cost[i]

            if currGas<0:
                start=i+1
                currGas=0

        return start if totalGas>=0 else -1