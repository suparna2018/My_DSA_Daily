from typing import List

class Solution:
    def isValidSudoku(self, nums: List[List[str]]) -> bool:
        def checkRow(nums,x):
            mp={}
            for i in range(9):
                if nums[x][i]==".":
                    pass
                elif nums[x][i] not in mp:
                    mp[nums[x][i]]=1
                else:
                    mp[nums[x][i]]+=1
                    if mp[nums[x][i]]>1:
                        print({nums[x][i]})
                        return False
            return True

        def checkCol(nums,y):
            mp={}
            for i in range(9):
                if nums[i][y]==".":
                    pass
                elif nums[i][y] not in mp:
                    mp[nums[i][y]]=1
                else:
                    mp[nums[i][y]]+=1
                    if mp[nums[i][y]]>1:
                        return False
            return True

        def checkSubBox(nums,start_row,start_col):
            seen = {}
            for i in range(3):
                for j in range(3):
                    num = nums[start_row + i][start_col + j]
                    if num != '.':
                        if num in seen:
                            return False
                        seen[num] = True
            return True

        for i in range(9):
            if not checkRow(nums,i):
                print("Row issue")
                return False
        for j in range(9):
            if not checkCol(nums,j):
                print("Column issue")
                return False
          # Check all 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not checkSubBox(nums, i, j):
                    print("Subbox issue")
                    return False
        return True

def TestCase():
    solution=Solution()
    input=      board = [["1","2",".",".","3",".",".",".","."],
                        ["4",".",".","5",".",".",".",".","."],
                        [".","9","8",".",".",".",".",".","3"],
                        ["5",".",".",".","6",".",".",".","4"],
                        [".",".",".","8",".","3",".",".","5"],
                        ["7",".",".",".","2",".",".",".","6"],
                        [".",".",".",".",".",".","2",".","."],
                        [".",".",".","4","1","9",".",".","8"],
                        [".",".",".",".","8",".",".","7","9"]
                        ]
    output= True

    res=solution.isValidSudoku(board)

    if res is output:
        print("Pass")
    else:
        print("Fail")

if __name__=="__main__":
    TestCase()
