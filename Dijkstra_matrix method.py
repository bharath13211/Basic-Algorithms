class Dijkstra:
    def shortestDistance(self, edges, vertices):
        if vertices<1:
            return []
        graph = [[0 for column in range(vertices)] for row in range(vertices)]
        for v1,v2,w in edges:
            graph[v1][v2] = w
        dist = [9999]*vertices
        dist[0] = 0
        sptSet = [False] * vertices
        for cout in range(vertices):
            #u = self.minDistance(dist, sptSet)
            mini = 9999
            for v in range(vertices):
                if dist[v] < mini and sptSet[v] == False:
                    mini = dist[v]
                    min_index = v
            sptSet[min_index] = True
            u = min_index
            for v in range(vertices):
                if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
        for i in range(len(dist)):
            if dist[i] == 9999:
                dist[i] = -1
        return dist