class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """

            A Tree made up of edges and nodes. 

            0 - 1
            2 - 3
        
        """
        
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()

        def isCyclicDFS(node, parent):
            
            visited.add(node)

            for neighbor in adj[node]:

                if neighbor not in visited:
                    if isCyclicDFS(neighbor, node):
                        return True
                else:
                    if parent != neighbor:
                        return True
            
            return False
                

        
        for node in range(n):
            if node not in visited:
                if isCyclicDFS(node, -1):
                    return False
        
        return True
        


