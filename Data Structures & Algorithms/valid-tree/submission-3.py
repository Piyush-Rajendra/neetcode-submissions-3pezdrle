class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # adj = [[] for _ in range(n)]
        # for a, b in edges:
        #     adj[a].append(b)  # [0] = [1]    [2] = [1, 3] 
        #     adj[b].append(a) # [1] = [2, 3]  [3]= [2, 1]
        
        # visited = set()

        # def dfs(node, parent):
        #     if node in visited:
        #         return False
            
        #     visited.add(node) # 0 , 1, 2, 3 
        #     for neighbor in adj[node]:  # 
        #         if neighbor == parent: # -1 # 0 # 1 
        #             continue
        #         if neighbor in visited: # 
        #             return False
        #         if not dfs(neighbor, node): 
        #             return False
        #     return True

        # if not dfs(0, -1):  # Start from node 0, parent is -1 (no parent)
        #     return False
        # return len(visited) == n      

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei == visited:
                    return False
                if not dfs(nei, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n




