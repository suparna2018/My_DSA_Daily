from sys import stdin
import sys 
import bisect
sys.setrecursionlimit(10**7)
def longestIncreasingSubsequence(arr, n) :
    temp=[]
    l=1
    temp.append(arr[0])
    for ind in range(1,n):
        if arr[ind]>temp[-1]:
            temp.append(arr[ind])
            l+=1
        else:
            index=bisect.bisect_left(temp,arr[ind])
            temp[index]=arr[ind]
    return l