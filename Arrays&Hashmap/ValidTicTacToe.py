"""
https://leetcode.com/problems/valid-tic-tac-toe-state/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days&status=TO_DO&difficulty=MEDIUM%2CHARD
"""



class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(s):
            # Check rows, columns, and diagonals for wins
            return (
                any(all(board[i][j] == s for j in range(3)) for i in range(3)) or  # rows
                any(all(board[j][i] == s for j in range(3)) for i in range(3)) or  # columns
                all(board[i][i] == s for i in range(3)) or                         # diagonal \
                all(board[i][2 - i] == s for i in range(3))                        # diagonal /
            )

            
        xCnt=oCnt=0
        for row in board:
            xCnt+=row.count("X")
            oCnt+=row.count("O")

        if xCnt<oCnt or xCnt-oCnt>1:
            return False

         # Check winning conditions
        xWins = win("X")
        oWins = win("O")

        # Both players can't win at the same time
        if xWins and oWins:
            return False
        
        # If X wins, it must be their turn (X has one more than O)
        if xWins and xCnt != oCnt + 1:
            return False

        # If O wins, they must have played last (equal counts)
        if oWins and xCnt != oCnt:
            return False

        return True