class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # 构建图
        nodes = {}
        for i in range(n):
            if i not in nodes:
                nodes[i] = []
        
        for edge in edges:
            nodes[edge[0]].append(edge[1]) 
            nodes[edge[1]].append(edge[0])
        # 遍历图
        visited = []
        count = 0
        def dfs(node):
            visited.append(node)
            if nodes[node]:
                for node in nodes[node]:
                    if node not in visited:
                        dfs(node)
        
        for node in nodes:
            if node not in visited:
                dfs(node)
                count += 1
        
        return count
