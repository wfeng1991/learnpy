class Solution:
    def nextGreaterElement1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<10 and n>pow(2,32)-1:
            return -1
        ns=list(str(n))
        i=len(ns)-1
        while i>0:
            if ns[i-1]<ns[i]:
                j,p=i,i
                while j<len(ns) and ns[j]>ns[i-1]:
                    if ns[p]>ns[j]:
                        p=j
                    j+=1
                ns[i-1],ns[p]=ns[p],ns[i-1]
                ns[i:]=sorted(ns[i:])
                return int(''.join(ns))
            i-=1
        return -1

    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        str_n = str(n)
        for i in range(len(str_n) - 2, -1, -1):
            if str_n[i] >= str_n[i+1]:
                continue
            else:
                found = str_n[i]
                result = ""
                for j in range(len(str_n) - 1, i, -1):
                    if str_n[j] > found:
                        next_great_sub = str_n[i+1:j] + str_n[i] + str_n[j+1:]
                        result = str_n[:i] + str_n[j] + next_great_sub[::-1]
                        return int(result) if int(result) < 2**31 -1 else -1
                else:
                    return -1
        return -1

print(Solution().nextGreaterElement(321))