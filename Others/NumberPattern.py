"""
print the number sequence::

   1
  23
 345
4567

"""



from math import *
from collections import *
from sys import *
from os import *
import sys

def printPattern(N):
    val = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            # Print space for alignment
            if i+j<=N:
                print(" ",end="")
            else:
                print(i,end="")  
                i+=1              
        print()  # Move to the next line after finishing one row
    return

Number=int(input())
printPattern(Number)
