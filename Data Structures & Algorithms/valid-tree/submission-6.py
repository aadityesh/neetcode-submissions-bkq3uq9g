from collections import deque
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
        que = deque()

        def isCyclicBFS(node, parent):
            
            que.append((node, parent))
            visited.add(node)

            while que:
                
                curNode, curParent = que.popleft()

                for neighbor in adj[curNode]:

                    if neighbor not in visited:
                        que.append((neighbor, curNode))
                        visited.add(neighbor)
                    else:
                        if curParent != neighbor:
                            return True
            
            return False
                
        if isCyclicBFS(0, -1): # Cycle Exists
            print("cycle exists")
            return False

        return len(visited) == n
        
        """

        Time - O(V + E)
        Space - O(2V)

        """


