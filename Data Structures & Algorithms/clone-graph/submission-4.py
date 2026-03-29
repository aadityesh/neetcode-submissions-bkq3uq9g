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
        
        if not node: return None

        queue = deque()
        visited = set()

        queue.append(node)
        visited.add(node)

        result = {}
        node_directory = {}
        newNode = None

        def bfs(curr):

            while queue:

                front = queue.popleft()

                curr = None
                if front.val not in node_directory.keys():
                    curr = Node(front.val)
                    node_directory[front.val] = curr
                else:
                    curr = node_directory[front.val]

                for neighbor in front.neighbors:

                    neigh = None
                    
                    if neighbor.val not in node_directory.keys():
                        neigh = Node(neighbor.val)
                        node_directory[neighbor.val] = neigh
                    else:
                        neigh = node_directory[neighbor.val]

                    curr.neighbors.append(neigh)
                    # neigh.neighbors.append(curr)
                    print(f"curr {curr.val} and neigh {neigh.val} and node_directory: {node_directory}")

                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

        bfs(node)
        print(node_directory)
        return node_directory[1]




            