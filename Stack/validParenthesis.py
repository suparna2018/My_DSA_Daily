class Solution:
    def isValid(self, s: str) -> bool:
        st=deque()
        for i in range(len(s)):
            if len(st)==0:
                st.append(s[i])
            elif (st[-1]=='['  and s[i]==']') or (st[-1]=='{' and s[i]=='}') or (st[-1]=='(' and s[i]==')'):
                st.pop()
            elif s[i]=='[' or s[i]=='{' or s[i]=='(':
                st.append(s[i])
            else:
                return False
        if len(st)==0:
            return True
        else:
            return False
