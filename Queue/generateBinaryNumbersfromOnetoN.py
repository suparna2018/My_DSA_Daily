"""
https://www.geeksforgeeks.org/problems/generate-binary-numbers-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
"""


#User function Template for python3
from queue import Queue
from collections import deque

#Function to generate binary numbers from 1 to N using a queue.
def generate(n):
    res=[]
    q=deque(["1"])
    s1=""
    while n>0:
        n-=1
        s1=q.popleft()
        res.append(s1)
        q.append(s1+"0")
        q.append(s1+"1")
        
    return res
        