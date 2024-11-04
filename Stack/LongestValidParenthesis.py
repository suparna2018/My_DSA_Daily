"""
https://leetcode.com/problems/longest-valid-parentheses/description/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days&status=TO_DO&difficulty=MEDIUM%2CHARD

"""



class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]

        for i in range(len(s)):
            if len(stack)>0:
                if stack[-1][0]=="(" and s[i][0]==")":
                    stack.pop(-1)
                else:
                    stack.append([s[i],i])
            else:
                stack.append([s[i],i])

        if len(stack)==0:
            return len(s)

        print(stack)
        prev=len(s)
        maxi=-1e9
        while len(stack)>0:
            x,ind=stack.pop()
            maxi=max(prev-ind-1,maxi)
            prev=ind
        
        maxi=max(prev,maxi)
        return maxi if maxi>-1e9 else 0