# https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implementing-floyd-warshall



class Solution:
	def shortest_distance(self, matrix):
		for i in range(len(matrix)):
    		    for j in range(len(matrix[0])):
    		        if(matrix[i][j]==-1):
    		            matrix[i][j]=1e9	
		# Floyed Warshall 
	    for k in range(len(matrix)):
    		for i in range(len(matrix)):
    		    for j in range(len(matrix[0])):
    		        matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
					
        for i in range(len(matrix)):
    		    for j in range(len(matrix[0])):
    		        if(matrix[i][j]==1e9):
    		            matrix[i][j]=-1
