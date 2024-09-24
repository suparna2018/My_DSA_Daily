"""
Problem statement
Given two strings, 'S' and 'T' with lengths 'M' and 'N', find the length of the 'Longest Common Subsequence'.

For a string 'str'(per se) of length K, the subsequences are the strings containing characters in the same relative order as they are present in 'str,' but not necessarily contiguous. Subsequences contain all the strings of length varying from 0 to K.

Example :
Subsequences of string "abc" are:  ""(empty string), a, b, c, ab, bc, ac, abc.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= M <= 10 ^ 3
0 <= N <= 10 ^ 3

Time Limit: 1 sec
Sample Input 1 :
adebc
dcadb
Sample Output 1 :
3
Explanation of the Sample Output 1 :
Both the strings contain a common subsequence 'adb', which is the longest common subsequence with length 3. 
Sample Input 2 :
ab
defg
Sample Output 2 :
0
Explanation of the Sample Output 2 :
The only subsequence that is common to both the given strings is an empty string("") of length 0.

"""

from sys import stdin

def lcs(s, t) :
	# def solve(ind1,ind2,dp):

	# 	if ind1==0 or ind2==0:
	# 		return 0

	# 	if dp[ind1][ind2]!=-1:
	# 		return dp[ind1][ind2]

	# 	# if both string match
	# 	if s[ind1-1]==t[ind2-1]:
	# 		dp[ind1][ind2]=1+solve(ind1-1,ind2-1,dp)
	# 		return dp[ind1][ind2]

	# 	# if dont match
	# 	dp[ind1][ind2]= max(solve(ind1-1,ind2,dp),solve(ind1,ind2-1,dp) )
	# 	return dp[ind1][ind2]


	n=len(s)
	m=len(t)
	prev=[0]*(m+1)
	curr=[0]*(m+1)
	
	for ind2 in range(m+1):
		prev[ind2]=0

	for ind1 in range(1,n+1):
		for ind2 in range(1,m+1):
			if s[ind1-1]==t[ind2-1]:
				curr[ind2]=1+prev[ind2-1]
			else:
				curr[ind2]= max(prev[ind2],curr[ind2-1])
		prev=curr[:]
		
	return prev[m]
