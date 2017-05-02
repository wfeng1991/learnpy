class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        i = 1
        mask = 1
        distance = 0
        while i <= 32:
            if (mask & x) != (mask & y):
                distance += 1
            x = x >> 1
            y = y >> 1
            i += 1
        return distance
