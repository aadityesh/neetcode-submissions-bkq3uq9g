class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for _ in range(n)]

        for course, preq in prerequisites:
            adj[course].append(preq)

        visited = set()
        path = [False] * n

        def DFS(node):

            visited.add(node)
            path[node] = True

            for neighbor in adj[node]:

                if neighbor not in visited:
                    if DFS(neighbor):
                        return True
                else:
                    if path[neighbor]:
                        return True

            path[node] = False
            return False
        
        for node in range(n):
            if node not in visited:
                if DFS(node):
                    return False

        return True



        