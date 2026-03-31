class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create a adjacency list for maintaining edges of connected edges
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(node):
            visited.add(node)

            for nei in adj[node]:
                if nei in visited:
                    continue
                dfs(nei)
        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count
        


     
        
        