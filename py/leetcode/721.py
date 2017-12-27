class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        import collections
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans

# class DSU:
#     def __init__(self):
#         self.p = list(range(10001))
#     def find(self, x):
#         if self.p[x] != x:
#             self.p[x] = self.find(self.p[x])
#         return self.p[x]
#     def union(self, x, y):
#         self.p[self.find(x)] = self.find(y)

# class Solution(object):
#     def accountsMerge(self, accounts):
#         dsu = DSU()
#         em_to_name = {}
#         em_to_id = {}
#         i = 0
#         for acc in accounts:
#             name = acc[0]
#             for email in acc[1:]:
#                 em_to_name[email] = name
#                 if email not in em_to_id:
#                     em_to_id[email] = i
#                     i += 1
#                 dsu.union(em_to_id[acc[1]], em_to_id[email])

#         ans = collections.defaultdict(list)
#         for email in em_to_name:
#             ans[dsu.find(em_to_id[email])].append(email)

#         return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]

