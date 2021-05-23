import sys
from bottle import post, request
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(dist[node])
    def minDistance(self, dist, sptSet):
 
        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        try:
            return min_index
        except TypeError:
            print ('Unable to find path')

    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)

# Driver program
if __name__ == '__main__':

    _ = float('inf')
    import numpy as np
    @post('/dijkstra', method='post')
    def my_form():
        n = request.forms.get('GetValue')
        M = np.random.randint(0,2,(n,n))
        np.fill_diagonal(M, 0)
        m = np.tril(M) + np.tril(M,-1).T
        print (m)
        print ("\n")
        for i in range(len(m)):
            for j in range (len(m[i])):
                if (m[i][j] == 1):
                    m[i][j] = np.random.randint(1,9)
        W = np.tril(m) + np.tril(m,-1).T
        print (W)
        print ("\n")
    g = Graph(n)
    g.graph = W
    a=int(input('Выберите вершину с которой хотите начать: '))
    g.dijkstra(a)
