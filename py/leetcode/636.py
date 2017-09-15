class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if not logs:
            return []
        res = [0]*n
        stack=[int(logs[0].split(':')[0])]
        pre=int(logs[0].split(':')[2])
        i=1
        while i<len(logs):
            log=logs[i].split(':')
            if log[1]=='start':
                if stack:
                    res[stack[-1]]+=int(log[2])-pre
                stack.append(int(log[0]))
                pre=int(log[2])
            else:
                res[stack[-1]]+=int(log[2])-pre+1
                stack.pop()
                pre=int(log[2])+1
            i+=1
        return res
        

print(Solution().exclusiveTime(3, ["0:start:0","1:start:2","2:start:3","2:end:4","1:end:5","0:end:6"]))