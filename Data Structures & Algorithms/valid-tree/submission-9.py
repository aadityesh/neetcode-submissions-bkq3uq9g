from collections import deque

class DSU:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, v):

        if self.parent[v] == v:
            return v
        
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, A, B):

        parentA, parentB = self.find(A), self.find(B)

        if parentA == parentB:
            return False
        
        else:

            if self.size[parentA] < self.size[parentB]:
                parentA, parentB = parentB, parentA
            
            self.parent[parentB] = parentA
            self.size[parentA] += self.size[parentB]

        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        obj = DSU(n)

        # Detects cycle
        for x, y in edges:
            if not obj.union(x, y):
                return False 
        
        # Detects if there are more than one component
        cnt = 0
        print(obj.parent)
        for node, parent in enumerate(obj.parent):
            if node == parent:
                cnt += 1
            
            if cnt > 1:
                return False

        return True
            
            
        
        


