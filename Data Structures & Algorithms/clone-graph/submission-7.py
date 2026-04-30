"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        
            Traverse over the Graph:
                For val: Node
                {
                    1: Node
                    2: Node
                }
        
        """

        if node is None: return None

        visited = set()
        mapping = {}

        # def BFS(node):

        #     q = deque([node])
        #     visited.add(node)

        #     while q:

        #         front = q.popleft()

        #         copy_node = None

        #         # Create current node
        #         if front not in mapping.keys():
        #             copy_node = Node(front.val)
        #             mapping[front] = copy_node

        #         else:
        #             copy_node = mapping[front]

        #         for neighbor in front.neighbors:

        #             if neighbor not in visited:
        #                 q.append(neighbor)
        #                 visited.add(neighbor)

        #             # Create neighbor node
        #             if neighbor not in mapping.keys():
        #                 neighbor_copy = Node(neighbor.val)
        #                 mapping[neighbor] = neighbor_copy
        #                 copy_node.neighbors.append(neighbor_copy)
        #             else:
        #                 copy_node.neighbors.append(mapping[neighbor])
        

        # BFS(node)


        def DFS(node):

            visited.add(node)
            copyNode = None

            if node not in mapping:
                copyNode = Node(node.val)
                mapping[node] = copyNode
            
            else:
                copyNode = mapping[node]

            
            for neighbor in node.neighbors:

                if neighbor not in mapping:
                    neighbor_copy = Node(neighbor.val)
                    mapping[neighbor] = neighbor_copy
                    copyNode.neighbors.append(neighbor_copy)
                else:
                    copyNode.neighbors.append(mapping[neighbor])


                if neighbor not in visited:
                    DFS(neighbor)


        
        DFS(node)
        return mapping[node]





                
            
