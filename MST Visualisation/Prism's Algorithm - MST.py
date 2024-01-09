#  ECIE 3101 Semester 1 Session 23/24
#  Group member:

#Mohammad Fakhrul Amin Bin Zainor 1911309
#Khaled Emad Khaled AlBawaliz 1828405
#Ridhwan Syaafi bin Ma’ahad 1917147
#Muhammad Harith Danial bin Bazli 1923499

#Prism's Algorithm MST Visualisation
#on 5 node of A,B,C,D,E with its edges
import sys
class Graph:
    def __init__(self, vertexNo, edge, node):
        self.edge = edge
        self.node = node
        self.vertexNo = vertexNo
        self.MST = []

    def printSolt(self):
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s -> %s: %s" % (s, d, w))

    def prismAlgo(self):
        visit = [0]*self.vertexNo
        edgeNum = 0
        visit[0] = True
        while edgeNum < self.vertexNo - 1:
            min = sys.maxsize
            for i in range(self.vertexNo):
                if visit[i]:
                    for j in range(self.vertexNo):
                        if ((not visit[j]) and self.edge[i][j]):
                            if min > self.edge[i][j]:
                                min = self.edge[i][j]
                                s = i 
                                d = j
            self.MST.append([self.node[s], self.node[d], self.edge[s][d]])
            visit[d] = True
            edgeNum += 1
        self.printSolt()


edge = [[0, 10, 20, 0, 0],
        [10, 0, 30, 5, 0],
        [20, 30, 0, 15, 6],
        [0, 5, 15, 0, 8],
        [0, 0, 6, 8, 0]]

node = ["A","B","C","D","E"]
g = Graph(5, edge, node)
g.prismAlgo()

