

from os import *
from sys import *
from collections import *
from math import *


# MCM Memoization
def matrixMultiplication(arr, n):
	def solve(i,j):
		if i==j:
			dp[i][j]=0
			return dp[i][j]
		if dp[i][j]!=-1:
			return dp[i][j]
		mini=1e9
		for k in range(i,j):
			steps=arr[i-1]*arr[k]*arr[j]+solve(i,k)+solve(k+1,j)
			mini=min(mini,steps)
			dp[i][j]=mini
		return dp[i][j]
		
	dp=[[-1]*n for _ in range(n)]
	return solve(1,n-1)


# MCM Tabulation

def matrixMultiplication(arr, n):
	dp=[[0]*n for _ in range(n)]
	
	for i in range(n-1,0,-1):
		for j in range(i+1,n):
			mini=1e9
			for k in range(i,j):
				steps=arr[i-1]*arr[k]*arr[j]+dp[i][k]+dp[k+1][j]
				mini=min(mini,steps)
			dp[i][j]=mini

	return dp[1][n-1]