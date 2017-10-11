class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols=[[0]*9 for _ in range(9)]
        rows=[[0]*9 for _ in range(9)]
        cubes=[[0]*9 for _ in range(9)]
        for i,r in enumerate(board):
            for j,v in enumerate(r):
                if v!='.':
                    num=int(v)-1
                    k=i//3*3+j//3
                    if cols[i][num] or rows[j][num] or cubes[k][num]:
                        return False
                    else:
                        cols[i][num] = rows[j][num] = cubes[k][num] = 1
        return True