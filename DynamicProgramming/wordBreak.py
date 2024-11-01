"""
https://leetcode.com/problems/word-break/description/?envType=problem-list-v2&envId=oizxjoit

"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        wordSet=set(wordDict)

        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i]=True
                    break
        return dp[n]