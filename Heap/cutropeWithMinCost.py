# https://www.naukri.com/code360/problems/connect-n-ropes-with-minimum-cost_630476?interviewProblemRedirection=true&company%5B%5D=PayPal,PayPal%20India%20Pvt%20Lt&sort_entity=company_count&sort_order=DESC&leftPanelTabValue=SUBMISSION


from sys import stdin,setrecursionlimit
import heapq
setrecursionlimit(10**7)

def connectRopes( arr, n) :
	cost=0
	heapq.heapify(arr)
	while len(arr)>1:
		fst=heapq.heappop(arr)
		sec=heapq.heappop(arr)
		cost+=fst+sec
		heapq.heappush(arr,fst+sec)

	return cost