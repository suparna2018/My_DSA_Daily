class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def GenPar(opened,closed,ans):
            if opened==0 and closed==0:
                res.append(ans)
                return 
            if opened>0:
                GenPar(opened-1,closed,ans+"(")
            if closed>0 and closed>opened:
                
                GenPar(opened,closed-1,ans+")")
        GenPar(n,n,"")
        return res
