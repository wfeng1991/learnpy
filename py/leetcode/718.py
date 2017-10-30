class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        cnt=0
        for i in range(len(A)):
            p,q=0,i
            while p<len(A) and q<len(B):
                while p<len(A) and q<len(B) and A[p]!=B[q]:
                    p+=1
                    q+=1
                t=0
                while p<len(A) and q<len(B) and A[p]==B[q]:
                    p+=1
                    q+=1
                    t+=1
                cnt=max(t,cnt)
        for i in range(len(B)):
            p,q=0,i
            while p<len(B) and q<len(A):
                while p<len(B) and q<len(A) and B[p]!=A[q]:
                    p+=1
                    q+=1
                t=0
                while p<len(B) and q<len(A) and B[p]==A[q]:
                    p+=1
                    q+=1
                    t+=1
                cnt=max(t,cnt)
        return cnt
   
    # Same idea of Longest Common Substring
    def findLength1(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B:
            return 0
        dp=[[0]*(len(A)+1) for _ in range(len(B)+1)]
        cnt=0
        for i,row in enumerate(dp):
            for j,c in enumerate(row):
                if i==0 or j==0:
                    continue
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    cnt = max(cnt,dp[i][j])
        return cnt

print(Solution().findLength([5,14,53,80,48], [50,47,3,80,83]))

        