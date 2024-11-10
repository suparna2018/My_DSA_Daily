"""
https://leetcode.com/problems/encode-and-decode-strings/description/?envType=problem-list-v2&envId=oizxjoit&status=TO_DO&difficulty=MEDIUM%2CHARD
"""

class Codec:
    def encode(self, strs: List[str]) -> str:
        newStrs=[]
        for ele in strs:
            newStrs.append(str(len(ele)))
            newStrs.append("#")
            newStrs.append(ele)
        res="".join(newStrs)
        print(res)
        return res
        
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=s.find('#',i)
            l=int(s[i:j])
            i=j+1
            res.append(s[i:i+l])
            i=i+l
        return res