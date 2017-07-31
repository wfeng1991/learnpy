class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.cnt=0
        def help(arr,i):
            if len(arr)==0:
                self.cnt+=1
            for x in arr:
                if x%i==0 or i%x==0:
                    help([y for y in arr if y!=x],i+1)
        help([x for x in range(1,N+1)],1)
        return self.cnt

print(Solution().countArrangement(7))



        