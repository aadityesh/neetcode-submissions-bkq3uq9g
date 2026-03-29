class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        """
            0 -> 1 -> 2 -> 0

            [[0, 1], [0, 2], [0, 3], [1, 4]]
            
            0 -> [1, 2, 3]
            1 -> [4]
        """

        adj_list = [[] for i in range(n)]

        for x, y in edges:
            if x == y: return False
            
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        print(adj_list)


        def dfs(curr, i):
            
            self.result.append(curr)
            self.visited[curr] = True

            for neighbor in adj_list[curr]:

                if i > 1 and neighbor == self.start:
                    self.status = False
                    return

                if not self.visited[neighbor]: 
                    dfs(neighbor, i + 1)



        
        for i in range(n):
            
            self.visited = [False] * n
            self.result = []
            self.status = True
            self.start = i

            dfs(i, 0)

            if self.status == False or len(self.result) != n: 
                print(self.start)
                return False

            # print(self.result)
            # if i in self.result[1::]: 
            #     print(self.result)
            #     print(i)
            #     return False
        
        return True
       



            
