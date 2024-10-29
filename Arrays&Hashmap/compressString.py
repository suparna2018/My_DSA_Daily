# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        cnt = 1
        i = 0
        
        while i < len(chars):
            # Start by adding the current character
            ans.append(chars[i])
            
            # Count consecutive occurrences of the same character
            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                cnt += 1
                i += 1
            
            # If there is more than one occurrence, append the count
            if cnt > 1:
                ans.extend(list(str(cnt)))
            
            # Move to the next character
            cnt = 1
            i += 1
        
        # Modify the original `chars` list in place
        chars[:] = ans
        
        # Return the length of the compressed list
        return len(ans)