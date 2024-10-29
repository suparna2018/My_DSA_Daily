'''Given a string s and a non-empty string p,
find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters
only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.
Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
'''

# ---------------------------------------------------------------------------------
# with counters


# def findAnagram(s,p):
#     m,n=len(s),len(p)
#     res=[]
#     if m<n:
#         return res
#     cnt1=Counter(p). #O(n)
#     cnt2=Counter(s[:n-1]) #str from [0,n-2] #O(n)
#     #start,end=0,0
#     #while start<end:
#     for i in range(n-1,m): #O(m)
#         cnt2[s[i]]+=1
#         if cnt1==cnt2: O(n)
#             res.append(i-(n-1))
#         cnt2[s[i-(n-1)]]-=1
#     return res
#     TC:O(n+m*)

# ----------------------------------------------------------------------------
# with two pointers

from collections import defaultdict

def findAnagrams(s,p):
    n,m=len(s),len(p)
    start,end=0,0
    mp=defaultdict(int)
    store=defaultdict(int)
    cnt=0
    res=[]
    for ele in p:
        store[ele]+=1

    while end<n:
        mp[s[end]]+=1
        if end-start+1==m:
            # there may be an answer
            if mp==store:
                res.append(start)
                cnt+=1

            mp[s[start]]-=1

            if mp[s[start]]==0:
                mp.pop(s[start])

            start+=1
        end+=1
    print(cnt)
    print(res)
    return cnt

# s="abab"
# p="ab"

s= "cbaebabacd" 
p="abc"
findAnagrams(s,p)
            





        