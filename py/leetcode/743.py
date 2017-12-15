class Solution(object):
    def networkDelayTime(self, times, N, K):
        import collections
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in range(1, N+1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1

Solution().networkDelayTime([[1,5,66],[3,5,55],[4,3,29],[1,2,9],[3,4,10],[3,1,3],[2,3,78],[1,4,98],[4,5,21],[5,2,19],[5,1,76],[4,1,65],[3,2,27],[5,3,23],[5,4,12],[2,1,36],[4,2,75],[2,4,11],[1,3,30],[2,5,8]],
5,
1)