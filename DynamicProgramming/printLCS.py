"""
Print Longest common subsequence.
"""

from sys import stdin

def lcs(s, t) :
	n=len(s)
	m=len(t)
	# prev=[0]*(m+1)
	# curr=[0]*(m+1)
	dp=[[0]*(m+1) for _ in range (n+1)]
	for ind1 in range(n+1):
		dp[ind1][0]=0
	for ind2 in range(m+1):
		dp[0][ind2]=0

	for ind1 in range(1,n+1):
		for ind2 in range(1,m+1):
			if s[ind1-1]==t[ind2-1]:
				dp[ind1][ind2]=1+dp[ind1-1][ind2-1]
			else:
				dp[ind1][ind2]= max(dp[ind1-1][ind2],dp[ind1-1][ind2-1])
		# prev=curr[:]
	for ele in dp:
		print(ele)
		print("\n")
	i=n
	j=m
	ans=""
	while i>0 or j>0:
		if(s[i-1]==t[j-1]):
			ans+=s[i-1]
			i-=1
			j-=1
		if dp[i-1][j]>dp[i][j-1]:
			i-=1
		else:
			j-=1
	print(ans[::-1])
	return dp[n][m]




# #main
# s = str(stdin.readline().rstrip())
# t = str(stdin.readline().rstrip())
s="adebc"
t="dcadb"


print(lcs(s, t))