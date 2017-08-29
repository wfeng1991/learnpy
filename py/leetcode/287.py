class Solution(object):
    def findDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        i=0
        while i<l:
            j=i+1
            while j<l:
                if nums[i]==nums[j]:
                    return nums[i]
                j+=1
            i+=1
        return 0
    # The main idea is the same with problem Linked List Cycle II,
    # https://leetcode.com/problems/linked-list-cycle-ii/. Use two 
    # pointers the fast and the slow. The fast one goes forward two
    #  steps each time, while the slow one goes only step each time.
    #  They must meet the same item when slow==fast. In fact, they meet
    #  in a circle, the duplicate number must be the entry point of the
    #  circle when visiting the array from nums[0]. Next we just need to 
    # find the entry point. We use a point(we can use the fast one before)
    #  to visit form begining with one step each time, do the same job to
    #  slow. When fast==slow, they meet at the entry point of the circle. 
    # The easy understood code is as follows.

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        fast=nums[nums[0]]
        slow=nums[0]
        while fast!=slow:
            fast=nums[nums[fast]]
            slow=nums[slow]
        fast=0
        while fast!=slow:
            fast=nums[fast]
            slow=nums[slow]
        return slow