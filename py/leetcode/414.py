class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1=None
        m2=None
        m3=None
        for x in nums:
            if not m1:
                m1=x
            elif x>m1:
                m3=m2
                m2=m1
                m1=x
            else:
                if (not m2 or x>m2) and x!=m1:
                    m3=m2
                    m2=x
                elif m2 and x<=m2:
                    if (not m3 or x>m3) and x!=m2:
                        m3=x
        return m3 if m3 is not None else m1
            
print(Solution().thirdMax([3,3,4,3,4,3,0,3,3]))