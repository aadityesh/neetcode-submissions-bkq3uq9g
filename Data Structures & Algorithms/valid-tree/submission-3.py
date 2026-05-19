class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """

            A Tree made up of edges and nodes. 

        
        """
        
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()


        def DFS(node, parent):
            
            visited.add(node)

            for neighbor in adj[node]:

                if neighbor not in visited:
                    if DFS(neighbor, node):
                        return True
                else:
                    if parent != neighbor:
                        return True
            
            return False
                

        
        for node in range(n):
            if node not in visited:
                if DFS(node, -1):
                    return False
        
        return True
        


