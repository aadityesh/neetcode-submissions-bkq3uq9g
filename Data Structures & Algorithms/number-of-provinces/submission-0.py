class Solution:
    def findCircleNum(self, a: List[List[int]]) -> int:

        V = len(a)
        visited = [False] * (V + 1)

        # get ADJ List
        adj_list = [[] for i in range(V + 1)]
        for i in range(V):
            for j in range(V):
                if not i == j and a[i][j] == 1:
                    adj_list[i+1].append(j+1)
        

        # dfs
        def dfs(curr):
            visited[curr] = True
            for i in adj_list[curr]:
                if not visited[i]: 
                    dfs(i)

        # Assume all the nodes can be start:
        provinces = 0
        for i in range(1, V + 1):
            if not visited[i]:
                dfs(i)
                provinces += 1

        return provinces
