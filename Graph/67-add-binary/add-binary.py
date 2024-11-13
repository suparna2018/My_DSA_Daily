class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxlen = max(len(a), len(b))
        a = a.zfill(maxlen)
        b = b.zfill(maxlen)
        
        res = []
        c = 0  
        for i in range(maxlen - 1, -1, -1):
            bit_a = int(a[i])  
            bit_b = int(b[i])  
     
            tot = bit_a + bit_b + c
            res.append(str(tot % 2))  
            c = tot // 2  
        
        if c:
            res.append(str(c))

        return ''.join(res[::-1])
