# https://www.naukri.com/code360/problems/split-bst_1376434?interviewProblemRedirection=true&company%5B%5D=Arcesium&sort_entity=recents&sort_order=DESC&leftPanelTabValue=PROBLEM

from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the TreeNode class structure

	class   TreeNode :
    	def __init__(self, val) :
        	self.val = val
        	self.left = None
        	self.right = None

'''

def splitBST(root,val):
	def dfs(root):
		if not root:
			return None,None
		if val>=root.val:
			
			leftTree,rightTree=dfs(root.right)
			root.right=leftTree
			return root,rightTree

		else:
			leftTree,rightTree=dfs(root.left)
			root.left=rightTree
			return leftTree,root

		return leftTree,rightTree
	return dfs(root)