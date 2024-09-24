from typing import List

class Solution:
    def shiftToNextChar(self,s):
        res=""
        for ele in s:
            if 'a'<=ele<='z':
                res=res+(chr( (((ord(ele)-ord('a') )+1)%26)+ord('a') ) )
            else:
                res=res+ele
        return res
    def shiftToPrevChar(self,s):
        res=""
        for ele in s:
            if 'a'<=ele<='z':
                res=res+(chr((( ( ord(ele)-ord('a') )-1)%26)+ord('a')) )
            else:
                res=res+ele
        return res


    def encode(self, strs: List[str]) -> str:
        modStr=[]
        for ele in strs:
            modStr.append(self.shiftToNextChar(ele))
        return modStr


    def decode(self, s: str) -> List[str]:
        modStr=[]
        for ele in s:
            modStr.append(self.shiftToPrevChar(ele))
        
        return modStr

def TestCase():
    solution=Solution()
    input= ["neet","code","love","you"]
    encodedStr= solution.encode(input)
    print(encodedStr)
    decodedStr=solution.decode(encodedStr)
    print(decodedStr)
    if (encodedStr!=input) and (decodedStr==input):
        print("Pass")
    else:
        print("Fail")

if __name__=="__main__":
    TestCase()


# TC:O(n)
# SC:O(n)