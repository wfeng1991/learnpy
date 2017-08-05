class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        row = len(board)
        col = len(board[0])
        _row = click[0]
        _col = click[1]
        if _row>=row or _col>=col:
            return board
        elif board[_row][_col]=='M':
            board[_row][_col]='X'
            return board
        q=[(_row,_col)]
        while q:
            b=q.pop()
            mn=0
            if b[0]-1>=0:
                if board[b[0]-1][b[1]]=='M':
                    mn+=1
            if b[1]-1>=0:
                if board[b[0]][b[1]-1]=='M':
                    mn+=1
            if b[0]+1<row:
                if board[b[0]+1][b[1]]=='M':
                    mn+=1
            if b[1]+1<col:
                if board[b[0]][b[1]+1]=='M':
                    mn+=1
            
            if b[0]-1>=0 and b[1]-1>=0:
                if board[b[0]-1][b[1]-1]=='M':
                    mn+=1
            if b[0]-1>=0 and b[1]+1<col:
                if board[b[0]-1][b[1]+1]=='M':
                    mn+=1
            if b[0]+1<row and b[1]+1<col:
                if board[b[0]+1][b[1]+1]=='M':
                    mn+=1
            if b[0]+1<row and b[1]-1>=0:
                if board[b[0]+1][b[1]-1]=='M':
                    mn+=1
            if mn==0:
                board[b[0]][b[1]]='B'
            else:
                board[b[0]][b[1]]=str(mn)
            if b[0]-1>=0:
                if mn==0 and board[b[0]-1][b[1]]=='E':
                    q.append((b[0]-1,b[1]))
            if b[1]-1>=0:
                if mn==0 and board[b[0]][b[1]-1]=='E':
                    q.append((b[0],b[1]-1))
            if b[0]+1<row:
                if mn==0 and board[b[0]+1][b[1]]=='E':
                    q.append((b[0]+1,b[1]))
            if b[1]+1<col:
                if mn==0 and board[b[0]][b[1]+1]=='E':
                    q.append((b[0],b[1]+1))
            
            if b[0]-1>=0 and b[1]-1>=0:
                if mn==0 and board[b[0]-1][b[1]-1]=='E':
                    q.append((b[0]-1,b[1]-1))
            if b[0]-1>=0 and b[1]+1<col:
                if mn==0 and board[b[0]-1][b[1]+1]=='E':
                    q.append((b[0]-1,b[1]+1))
            if b[0]+1<row and b[1]+1<col:
                if mn==0 and board[b[0]+1][b[1]+1]=='E':
                    q.append((b[0]+1,b[1]+1))
            if b[0]+1<row and b[1]-1>=0:
                if mn==0 and board[b[0]+1][b[1]-1]=='E':
                    q.append((b[0]+1,b[1]-1))

        return board
