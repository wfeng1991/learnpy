class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # - 00  dead (next) <- dead (current)
        # - 01  dead (next) <- live (current)  
        # - 10  live (next) <- dead (current)  
        # - 11  live (next) <- live (current) 
        row=len(board)
        col=len(board[0])
        res=[[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                livecells=0
                if i>0:
                    livecells+=board[i-1][j]&1
                    if j>0:
                        livecells+=board[i-1][j-1]&1
                    if j+1<col:
                        livecells+=board[i-1][j+1]&1
                if j>0:
                        livecells+=board[i][j-1]&1

                if i+1<row:
                    livecells+=board[i+1][j]&1
                    if j+1<col:
                        livecells+=board[i+1][j+1]&1
                    if j>0:
                        livecells+=board[i+1][j-1]&1
                if j+1<col:
                        livecells+=board[i][j+1]&1
                    
                if board[i][j] == 1 and livecells >= 2 and livecells <= 3:  
                    board[i][j] = 3
                if board[i][j] == 0 and livecells == 3:
                    board[i][j] = 2 

        for i in range(row):
            for j in range(col):
                board[i][j] >>= 1
            
        print(board)

Solution().gameOfLife([[1]])