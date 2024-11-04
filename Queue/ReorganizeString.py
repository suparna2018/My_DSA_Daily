"""
https://leetcode.com/problems/reorganize-string/description/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days&status=TO_DO&difficulty=MEDIUM%2CHARD
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        mp={}
        res=[]
        for ele in s:
            mp[ele]=mp.get(ele,0)+1

        heap=[]
        for ele in mp:
            heapq.heappush(heap,(-mp[ele],ele))
        while len(heap)>=2:
            first,el1=heapq.heappop(heap)
            second,el2=heapq.heappop(heap)

            res.append(el1)
            res.append(el2)

            if first+1<0:
                heapq.heappush(heap,(first+1,el1))
            if second+1<0:
                heapq.heappush(heap,(second+1,el2))

        if len(heap)>0:
            first,el1=heapq.heappop(heap)
            if -first>1:
                return ""
            else:
                res.append(el1)

        return "".join(res)