class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])

        def BS(nums,lo,hi):
            mid=int((lo+hi)/2)
            if lo>hi:
                return False
            elif(nums[mid]==target):
                return True
            elif nums[mid]>target:
                return BS(nums,lo,mid-1)
            else:
                return BS(nums,mid+1,hi)

        for i in range(n):
            if matrix[i][0]<=target<= matrix[i][m-1]:
                print("ok",i)
                return BS(matrix[i],0,m-1)
                      
        return False