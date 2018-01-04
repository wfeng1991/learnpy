class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        idx=0
        l=len(gas)
        while idx<l:
            gas_remain=0
            offset=0
            while offset<l and (gas_remain+gas[idx%l])>=cost[idx%l]:
                gas_remain=gas_remain+gas[idx%l]-cost[idx%l]
                idx+=1
                offset+=1
            if offset==l:
                return idx-offset
            else:
                idx+=1
        return -1

print(Solution().canCompleteCircuit([1,2,3,3],[2,1,5,1]))