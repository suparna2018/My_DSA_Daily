"""
https://leetcode.com/problems/maximum-swap/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days&status=TO_DO&difficulty=MEDIUM%2CHARD
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr=str(num)
        number=[int(d) for d in numStr]

        copy=(sorted(number))[::-1]

        print(copy)

        for i in range(len(number)):
            if number[i]!=copy[i]:
                break
            
        ind = len(number) - 1 - number[::-1].index(copy[i])
        number[ind],number[i]=number[i],number[ind]
        print(number)
        res=[str(d) for d in number]
        res="".join(res)

        return int(res)