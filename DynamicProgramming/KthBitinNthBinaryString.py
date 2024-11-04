"""
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days&status=TO_DO&difficulty=MEDIUM%2CHARD
"""



class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def Calc(prev,n):
            if n<2:
                return prev  
            
            last = ''.join('0' if v == '1' else '1' for v in prev[::-1])
            for v in last:
                if v=="1":
                    v="0"
                else:
                    v="1"

            S=prev +"1"+str(last)
            return Calc(S,n-1)
        
        prev="0"
        # val=Calc(S,n)
        for i in range(n):
            last = ''.join('0' if v == '1' else '1' for v in prev[::-1])
            for v in last:
                if v=="1":
                    v="0"
                else:
                    v="1"

            S=prev +"1"+str(last)
            prev=S
        # print(prev)
        return prev[k-1]