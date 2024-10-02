# https://leetcode.com/problems/bag-of-tokens/description/?envType=problem-list-v2&envId=e9snhf4h&status=TO_DO&difficulty=MEDIUM

class Solution:
    def bagOfTokensScore(self, token: List[int], power: int) -> int:
        i,j=0,len(token)-1
        token.sort()
        maxScore=0
        score=0

        while i<=j:
            # face up gain Score
            if power>=token[i]:
                power-=token[i]
                score+=1
                i+=1
                print(power,score,i,j)
            # face down loose score
            elif score>=1:
                score-=1
                power+=token[j]
                j-=1
                print(power,score,i,j)
            else:
                i+=1
                j-=1
            maxScore=max(maxScore,score)
        return maxScore