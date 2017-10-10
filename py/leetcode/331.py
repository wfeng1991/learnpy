class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes=preorder.split(',')
        l=len(nodes)
        stack=[]
        for i,n in enumerate(nodes):
            if i==l-1 and n=='#' and len(stack)==0:
                return True
            if n=='#':
                if len(stack)>0:
                    stack.pop()
                else:
                  return False  
            else:
                stack.append(n)
        return False