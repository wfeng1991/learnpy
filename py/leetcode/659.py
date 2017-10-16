class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq={}
        appendnum={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        for n in nums:
            if freq[n]==0:
                continue
            if appendnum.get(n,0)>0:
                appendnum[n]-=1
                appendnum[n+1]=appendnum.get(n+1,0)+1
            elif freq.get(n+1,0)>0 and freq.get(n+2,0)>0:
                freq[n+1]-=1
                freq[n+2]-=1
                appendnum[n+3]=appendnum.get(n+3,0)+1
            else:
                return False
            freq[n]-=1
        return True
print(Solution().isPossible([1,2,3,3,4,5]))