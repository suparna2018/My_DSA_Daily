
from typing import List


def longestStrChain(arr: List[str]) -> int:
    def isPre(s1,s2):
        if len(s1)!=len(s2)+1:
            return False
        first=0
        second=0
        # Traverse both strings to see if s2 can become s1 by inserting exactly one character
        while first < len(s1):
            if second < len(s2) and s1[first] == s2[second]:
                second += 1
            first += 1

        # If we successfully traversed s2 (second reached the end), return True
        return second == len(s2)

    n=len(arr)
    dp=[1]*n
    arr.sort(key=len)
    for ind in range(n):
        for prev in range(ind):
            if isPre(arr[ind],arr[prev]) and dp[ind]<dp[prev]+1:
                dp[ind]=dp[prev]+1
    return max(dp)



