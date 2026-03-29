class Solution:
    def findCircleNum(self, a: List[List[int]]) -> int:

        V = len(a)
        visited = [False] * (V)

        # get ADJ List
        # adj_list = [[] for i in range(V)]
        # for i in range(V):
        #     for j in range(V):
        #         if not i == j and a[i][j] == 1:
        #             adj_list[i].append(j)
        

        # dfs (adj_list)
        # def dfs(curr):
        #     # res.append(curr) : no need for this
        #     visited[curr] = True
        #     for i in adj_list[curr]:
        #         if not visited[i]: 
        #             dfs(i)

        def dfs(curr):
            visited[curr] = True
            for i in range(V):
                if not visited[i] and a[curr][i]: 
                    dfs(i)

        # Assume all the nodes can be start:
        provinces = 0
        for i in range(V):
            if not visited[i]:
                dfs(i)
                provinces += 1

        return provinces
