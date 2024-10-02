# https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/description/?envType=problem-list-v2&envId=e9snhf4h&status=TO_DO&difficulty=MEDIUM

class Solution:
    def getMinSwaps(self, nums: str, k: int) -> int:
        def minSwapsToConvert(num1, num2) -> int:
            num1 = list(num1)  # Convert to list to make swapping easier
            swaps = 0
            
            for i in range(len(num2)):
                # Find the position of num2[i] in num1 starting from i
                j = i
                while num1[j] != num2[i]:
                    j += 1
                while j > i:
                    # Swap the adjacent elements
                    num1[j], num1[j-1] = num1[j-1], num1[j]
                    j -= 1
                    swaps += 1
            
            return swaps

        def nextPermutation(num):
            # print(num)
            peak=0
            for i in range(len(num)-1,-1,-1):
                if num[i]>num[i-1]:
                    peak=i-1
                    break
                

            for i in range(len(num)-1,peak,-1):
                if num[i]>num[peak]:
                    num[i],num[peak]=num[peak],num[i]
                    break

            num=num[:peak+1]+num[peak+1:][::-1]
            # print(num)
            return num


        num=nums
        arr=[ele for ele in nums]
        for i in range(k):
            arr=nextPermutation(arr) 
        # print(arr)   

        # Get numver of swaps
        arr1=[ele for ele in nums]
        arr2=[ele for ele in arr]
        return minSwapsToConvert(arr1,arr2)