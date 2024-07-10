from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        res=[]
        for word in words:
            sortedWord=tuple(sorted(word))
            mp[sortedWord].append(word)
        res=list(mp.values())
        return res
    
def TestCase():
    solution=Solution()
    input= ["act","pots","tops","cat","stop","hat"]
    output= [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]

    res=solution.groupAnagrams(words=input)
    for ele in res:
        ele=sorted(ele)
    for ele in output:
        ele=sorted(ele)
    
    # print(res)
    # print(output)

    def isEqual(res,output ):
        for ele in res:
            if ele not in output:
                print("Fail")
                return
            
        for ele in output:
            if ele not in res:
                print("Fail")
                return     
        print("Pass")


    isEqual(res,output)
    return

if __name__=="__main__":
    TestCase()