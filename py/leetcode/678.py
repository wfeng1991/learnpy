class Solution:
    def checkValidString1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def help(s,stack,idx):
            if len(s)==idx and len(stack)==0:
                return True
            elif len(s)==idx and len(stack)!=0:
                return False
            t=s[idx]
            if t=='(':
                return help(s,stack+['('],idx+1)
            if t=='*' and stack:
                return help(s,stack+['('],idx+1) or help(s,stack[:-1],idx+1) or help(s,stack,idx+1)
            elif t=='*' and not stack:
                return help(s,stack+['('],idx+1) or help(s,stack,idx+1)
            elif stack:
                return help(s,stack[:-1],idx+1)
            else:
                return False
        return help(s,[],0)

    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)
        return lo == 0


print(Solution().checkValidString("((*)(*))(((*))"))
