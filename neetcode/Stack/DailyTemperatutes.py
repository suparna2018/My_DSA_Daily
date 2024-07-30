from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=deque()
        res=[]
        res.append(0)
        for i in range(len(temperatures)-1,-1,-1):
            print(i)
            if not st:
                st.append([temperatures[i],i])
            else:
                while st and st[-1][0]<=temperatures[i]:
                    ele=st.pop()
                
                if not st:
                    res.append(0)
                else:
                    element=st[-1]
                    res.append(element[1]-i)
                st.append([temperatures[i],i])

        # print(res)
        return res[::-1]