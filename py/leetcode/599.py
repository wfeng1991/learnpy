class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        rest = []
        for i,s1 in enumerate(list1):
            for j,s2 in enumerate(list2):
                if s1==s2:
                    rest.append([i+j,s1])
        m = rest[0][0]
        for t in rest:
            if t[0]<=m:
                m=t[0]
        r = []
        for t in rest:
            if t[0]==m:
                r.append(t[1])
        return r
        


print(Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]))
                