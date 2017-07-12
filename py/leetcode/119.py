class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        r=[1 for x in range(0, rowIndex+1)]
        preRow = []
        for j in range(1,rowIndex+2):
            for i in range(0,j):
                if i==0 or i==j-1:
                    r[i]=1
                else:
                    r[i]=preRow[i]+preRow[i-1]
            preRow = [x for x in r]
        return r

print(Solution().getRow(0))