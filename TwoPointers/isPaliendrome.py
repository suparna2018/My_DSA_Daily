import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def cleanString(inputStr):
            translator = str.maketrans('', '', string.punctuation + ' ')
            return inputStr.translate(translator).replace(' ', '').lower()

        string1=cleanString(s)
        n=len(string1)
        for i in range(n):
            if string1[i]==string1[n-1-i]:
                pass
            else:
                return False
        return True
        