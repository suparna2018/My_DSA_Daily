class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxlen = max(len(a), len(b))
        a = a.zfill(maxlen)
        b = b.zfill(maxlen)
        
        res = []
        c = 0  # Initialize carry to 0

        # Iterate from the end to the beginning
        for i in range(maxlen - 1, -1, -1):
            bit_a = int(a[i])  # Convert character to integer
            bit_b = int(b[i])  # Convert character to integer

            # Total sum of both bits and the carry
            tot = bit_a + bit_b + c
            res.append(str(tot % 2))  # Append the result bit
            c = tot // 2  # Update carry

        # If there's a carry left after the loop, append it
        if c:
            res.append(str(c))

        # The result is currently reversed, so reverse it back
        return ''.join(res[::-1])
