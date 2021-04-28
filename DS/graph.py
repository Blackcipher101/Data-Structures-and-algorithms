class AdjacencyList:
    def __init__(self):
        self.List = {}
    def addEdge(self, source, destination):
        if source in self.List.keys():
            self.List[source].append(destination)
        else:
            self.List[source] = [destination]
    def printList(self):
        for i  in self.List:
            print(i,'->',' -> '.join([str(j) for j in self.List[i]]))

al = AdjacencyList()
al.addEdge('A', 'B')
al.addEdge('A', 'C')
al.addEdge('B', 'E')
al.addEdge('B', 'D')
al.addEdge('D', 'E')
al.addEdge('C', 'D')
al.addEdge('D', 'A')
al.printList()