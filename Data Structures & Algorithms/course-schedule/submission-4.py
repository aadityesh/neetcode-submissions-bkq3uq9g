class Solution:
    def canFinish(self, n: int, prereq: List[List[int]]) -> bool:
        
        # course_dict = {}

        # for x, y in prereq:

        #     if (y in course_dict and course_dict[y] == x) or (x == y):
        #         return False

        #     course_dict[x] = y
        
        # return True

        adj_list = [[] for i in range(n)]

        for course, pre in prereq:
            adj_list[course].append(pre)
    

        def dfs(curr):

            print(curr)
            self.visited[curr] = True

            for neighbor in adj_list[curr]:

                if self.visited[neighbor] and neighbor == self.start:
                    self.status = False
                    return

                if not self.visited[neighbor]: 
                    dfs(neighbor)

        for i in range(n):

            self.status = True
            self.start = i
            self.visited = [False] * (n)

            dfs(i)

            if not self.status: return False
        
        return True









        