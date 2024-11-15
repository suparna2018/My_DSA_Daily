class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=1
        digits=digits[::-1]

        for i in range(len(digits)):
            digits[i]=digits[i]+c
            if digits[i]>9:
                digits[i]=0
                c=1
            else:
                c=0
        if c==1:
            digits.append(c)

        return digits[::-1]

        