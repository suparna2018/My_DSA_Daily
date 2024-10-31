class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dp(ind):
            if ind == n:  # Base case: reached end of string
                return 1
            if s[ind] == "0":  # Invalid if the current segment starts with '0'
                return 0
            if ind in memo:  # Return memoized result if available
                return memo[ind]

            # Take 1 character
            res = dp(ind + 1)
            
            # Take 2 characters
            if ind < n - 1 and (
                (s[ind] == "1" and s[ind + 1] in "0123456789") or
                (s[ind] == "2" and s[ind + 1] in "0123456")
            ):
                res += dp(ind + 2)

            memo[ind] = res  # Memoize result
            return res

        n = len(s)
        memo=[0]*(n+1)
        memo[n]=1
        
        for ind in range(n-1,-1,-1):
            if s[ind] == "0":  # Invalid if the current segment starts with '0'
                memo[ind]=0
            else: 
                # Take 1 character
                res =memo[ind+1] 
                
                # Take 2 characters
                if ind < n - 1 and (
                    (s[ind] == "1" and s[ind + 1] in "0123456789") or
                    (s[ind] == "2" and s[ind + 1] in "0123456")
                ):
                    res +=memo[ind+2] 

                memo[ind] = res
            
        return memo[0]