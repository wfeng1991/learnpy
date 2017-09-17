class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        n=''
        p=''
        for c in s:
            if c=='[':
                if len(p)>0:
                    stack.append(p)
                    p=''
                if len(n)>0:
                    stack.append(n)
                    n=''
                continue
            if c.isalpha():
                p+=c
            elif len(p)>0:
                stack.append(p)
                p=''
            if c.isdigit():
                n+=c
            elif len(n)>0:
                stack.append(n)
                n=''
            if c==']':
                _s=''
                ss=stack.pop()
                while ss.isalpha():
                    _s=ss+_s
                    ss=stack.pop()
                num=ss
                _s=_s*int(num)
                stack.append(_s)
        return ''.join(stack)+p

print(Solution().decodeString('2[2[b]]'))