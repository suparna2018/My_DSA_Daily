class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cur = 0
        oneAhead = 1
        twoAhead = 1

        for ind in range(n - 1, -1, -1):
            if s[ind] == "0":  # If current character is '0', no valid decoding
                cur = 0
            else:
                # Single character decoding
                cur = oneAhead
                
                # Two character decoding if it's within the valid range
                if ind < n - 1 and (
                    s[ind] == "1" or (s[ind] == "2" and s[ind + 1] in "0123456")
                ):
                    cur += twoAhead

            # Move pointers
            twoAhead = oneAhead
            oneAhead = cur

        return oneAhead