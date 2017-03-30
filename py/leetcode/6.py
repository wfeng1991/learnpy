class Solution(object):
     def convert(self, s, rows):
        if rows == 1:
            return s
        res = []
        for x in range(1, rows+1):
            res.append([])
        change = True
        idx = 0
        for i,c in enumerate(s):          
            if change:
                res[idx].append(c)
                idx = idx + 1
                if idx == rows - 1:
                    idx = 0
                    change = False
            else:
                res[rows - idx - 1].append(c)
                idx = idx + 1
                if idx == rows - 1:
                    idx = 0
                    change = True
        a = ''
        for x in res:
            a = a + ''.join(x)
        return a

result = Solution()
result = result.convert("AB", 1)
print(result)