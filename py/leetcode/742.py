# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        import collections
        graph=collections.defaultdict(list)
        def dfs(root,node):
            if root:
                graph[root].append(node)
                graph[node].append(root)
                dfs(root.left,root)
                dfs(root.right,root)
        dfs(root,None)
        queue=[node for node in graph if node!=None and node.val==k]
        seen=set(queue)
        while queue:
            n=queue[0]
            queue=queue[1:]
            if len(graph[n])<=1:
                return n.val
            for node in graph[n]:
                if node and node not in seen:
                    seen.add(node)
                    queue.append(node)
        
