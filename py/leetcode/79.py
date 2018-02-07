class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def exist0(board,x,y,word,idx):
            if x==len(board) or y==len(board[0]) or x<0 or y<0:
                return False
            if idx==len(word)-1 and board[x][y]==word[idx]:
                return True
            if idx<len(word) and board[x][y]==word[idx]:
                board[x][y] += "*"
                res = exist0(board,x-1,y,word,idx+1) or exist0(board,x+1,y,word,idx+1) or exist0(board,x,y+1,word,idx+1) or exist0(board,x,y-1,word,idx+1)
                board[x][y] = board[x][y][0]
                return res
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if exist0(board,i,j,word,0):
                    return True
        return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))