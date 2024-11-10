"""
https://leetcode.com/problems/distinct-subsequences/description/

"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def distinctSubsequences(str1: str, sub: str) -> int:
            n, m = len(str1), len(sub)
            # Initialize DP array with zeroes
            dp = [[0] * (m + 1) for _ in range(n + 1)]
            
            # Base case: If `sub` is an empty string, there's exactly 1 way to match it (by deleting all characters of `str1`).
            for i in range(n + 1):
                dp[i][0] = 1
            
            # Fill the DP table
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    # If the characters match, we can either:
                    # 1. Take the match (dp[i-1][j-1])
                    # 2. Skip the current character of str1 (dp[i-1][j])
                    if str1[i - 1] == sub[j - 1]:
                        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                    else:
                        # If they don't match, we can only skip the current character of str1
                        dp[i][j] = dp[i - 1][j]
            
            # The result is the number of distinct subsequences of `sub` in `str1`
            return dp[n][m]
        return distinctSubsequences(s,t)
