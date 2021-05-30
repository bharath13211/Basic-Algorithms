from collections import defaultdict

class CriticalLink:
    #def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    def criticalLink(self, n : int, links : [[int]]) -> int:
        visited = [None]*n
        reach = [None]*n
        g = defaultdict(list)
        for e in links:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        
        def dfs(cur, depth, pre):
            visited[cur] = depth
            reach[cur] = depth 
            for nxt in g[cur]:
                if visited[nxt] == None:
                    dfs(nxt, depth+1, cur)
                    reach[cur] = min(reach[cur], reach[nxt])
                elif nxt != pre:
                    reach[cur] = min(reach[cur], visited[nxt])
            if pre != None and visited[cur] == reach[cur]:
                res.append([pre,cur])
            return
        
        res = []
        dfs(0, 0, None)
        total = len(res)
        return total