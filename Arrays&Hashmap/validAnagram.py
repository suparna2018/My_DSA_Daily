
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp={}
        if len(s)!=len(t):
            return False
        for ele in s:
            if ele in mp:
                mp[ele]+=1
            else:
                mp[ele]=1
        for ele in t:
            if ele in mp:
                mp[ele]-=1
                if mp[ele]==0:
                    mp.pop(ele)
        if not mp:
            return True
        return False
def testCase():
    input1="qwerty"
    input2="ytrewq"
    solution=Solution()
    result=solution.isAnagram(input1,input2)
    if result==True:
        print("Pass")
    else:
        print("Fail")

if __name__=="__main__":
    testCase()
                