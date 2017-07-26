class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def alone(m,x,y,xl,yl):
            if x+1<xl and not m[x+1][y]:
                return False
            if y+1<yl and not m[x][y+1]:
                return False
            if x-1>=0 and not m[x-1][y]:
                return False
            if y-1>=0 and not m[x][y-1]:
                return False
            return True
        cnt = 0
        xl = len(board)
        yl = len(board[0])
        m = [[True for i in range(0,yl)] for i in range(0,xl)]
        for x,row in enumerate(board):
            for y,bs in enumerate(row):
                if bs=='X' and m[x][y] and alone(m,x,y,xl,yl):
                    cnt+=1
                    m[x][y]=False
                elif bs=='X':
                    m[x][y]=False
        return cnt

print(Solution().countBattleships([['X','.'],['.','X']]))
                