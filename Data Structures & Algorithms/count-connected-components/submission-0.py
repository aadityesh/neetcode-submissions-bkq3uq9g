class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = [False] * n
        adj = [[] for i in range(n)]

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        
        def dfs(curr):

            visited[curr] = True

            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    dfs(neighbor)

        cnt = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                cnt += 1
        
        return cnt


        