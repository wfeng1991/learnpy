class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        r = []
        for i in range(0, numRows):
            t=[]
            for j in range(0,i+1):
                if j==0 or j==i:
                    t.append(1)
                else:
                    t.append(r[i-1][j-1]+r[i-1][j])
            r.append(t)
        return r

print(Solution().generate(6))
                
