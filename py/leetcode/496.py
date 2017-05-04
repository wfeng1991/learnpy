class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(findNums)
        i = 0
        r = []
        for c in findNums:
            r.append(-1)
        while i < l:
            before = True
            for n in nums:
                if before and findNums[i] == n:
                    before = False
                    continue
                if not before and findNums[i] < n:
                    r[i] = n
                    break
            i += 1
        return r

s = Solution()
print(s.nextGreaterElement([4,1,2],[1,3,4,2]))