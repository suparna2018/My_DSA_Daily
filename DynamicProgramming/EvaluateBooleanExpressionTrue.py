# https://www.naukri.com/code360/problems/problem-name-boolean-evaluation_1214650?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTabValue=PROBLEM

def evaluateExp(exp: str) -> int:  
    def solve(i,j,isTrue,dp):
        if i>j:
            return 0

        elif i==j:
            if isTrue==1:
                return int(exp[i]=='T')
            else:
                return int(exp[i]=='F')

        if dp[i][j][isTrue]!=-1:
            return dp[i][j][isTrue]

        ways=0
        for ind in range(i+1,j,2):
            lF=solve(i,ind-1,0,dp)
            lT=solve(i,ind-1,1,dp)
            rF=solve(ind+1,j,0,dp)
            rT=solve(ind+1,j,1,dp)

            if exp[ind]=='&':
                if isTrue:
                    ways=(ways+(lT*rT)%mod)
                else:
                    ways=(ways+(lT*rF)%mod)+(lF*rT)%mod+(lF*rF)%mod
            elif exp[ind]=='|':
                if isTrue:
                    ways=(ways+(lT*rF)%mod)+(lF*rT)%mod+(lT*rT)%mod
                else:
                    ways=(ways+(lF*rF)%mod)
            elif exp[ind]=='^':
                if isTrue:
                    ways=(ways+(lT*rF)%mod)+(lF*rT)%mod
                else:
                    ways=(ways+(lT*rT)%mod)+(lF*rF)%mod

        dp[i][j][isTrue]=ways%mod
        return dp[i][j][isTrue]

    n=len(exp)
    mod=1000000007
    dp=[[[-1]*2 for i in range(n)] for _ in range(n)]
    return solve(0,n-1,1,dp)
