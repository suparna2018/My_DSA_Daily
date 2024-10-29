# https://www.naukri.com/code360/problems/largest-subarray-with-equal-number-of-0s-and-1s_839812?interviewProblemRedirection=true&page=2&company%5B%5D=PayPal&company%5B%5D=PayPal%20India%20Pvt%20Lt&difficulty%5B%5D=Medium&difficulty%5B%5D=Hard&difficulty%5B%5D=Ninja&sort_entity=company_count&sort_order=DESC&leftPanelTabValue=PROBLEM

from os import *
from sys import *
from collections import *
from math import *

def findSubarray(arr, n):
    mp={}
    ans=0
    cnt=0
    for i in range(n):
        if arr[i]==0:
            cnt-=1
        else:
            cnt+=1
        if cnt==0:
            ans=max(ans,i+1)
        elif cnt in mp:
            ans=max(ans,i-mp[cnt])
        else:
            mp[cnt]=i

    return ans
        