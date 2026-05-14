from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)] 
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visited = set()

        def BFS(node):

            que = deque([node])
            visited.add(node)

            while que:
                curr = que.popleft()

                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        que.append(neighbor)
                        visited.add(neighbor)

        cnt = 0
        for node in range(n):
            if node not in visited:
                BFS(node)
                cnt += 1
        
        return cnt



        