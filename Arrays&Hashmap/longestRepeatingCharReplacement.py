"""
https://leetcode.com/problems/longest-repeating-character-replacement/?envType=problem-list-v2&envId=oizxjoit&difficulty=MEDIUM%2CHARD
"""

from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        maxi=-1e9
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            i,j,replaced,ans=0,0,0,1
            while j<n:
                if(s[j]==c):j+=1
                elif(replaced<k):
                    j+=1
                    replaced+=1
                elif s[i]==c:
                    i+=1
                else:
                    replaced-=1
                    i+=1
                ans=max(ans,j-i)
            maxi=max(maxi,ans)
        return maxi