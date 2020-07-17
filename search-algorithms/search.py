# Fernando Lima - UEMS
# 36716
# lnfernandobr@gmail.com

class Search:
    def __init__(self, initialNode, finalNode, maxDepth):
        self.initialNode = initialNode
        self.finalNode = finalNode
        self.maxDepth = maxDepth

    visited = []

    graph = {
        '1': ['2', '3'],
        '2': ['1', '4'],
        '3': ['1', '4', '6', '7'],
        '4': ['2', '3', '5'],
        '5': ['4', '8'],
        '6': ['3', '11', '12'],
        '7': ['3', '13'],
        '8': ['5', '9'],
        '9': ['8', '10'],
        '10': ['9', '11'],
        '11': ['6', '10', '12'],
        '12': ['6', '11', '13'],
        '13': ['7', '12', '14', '15'],
        '14': ['13'],
        '15': ['13', '16', '19'],
        '16': ['15', '17'],
        '17': ['16', '18'],
        '18': ['17'],
        '19': ['15', '20'],
        '20': ['19'],
    }

    def run_dfsInteractive(self, start, goal, limit):
        for newLimit in range(limit + 1):
            if self.run_dls(start, goal, newLimit):
                return True

        return False

    def dfsInteractive(self):
        if self.run_dls(self.initialNode, self.finalNode, self.maxDepth):
            print("O cidade visitada de número ", self.finalNode, " foi encontrada e visitada!")

        else:
            print("A cidade de numero ", self.finalNode, " não foi encontrada")

    def clear(self):
        self.visited = []

    def print(self):
        print(' '.join(map(str, self.visited)))

        if self.finalNode not in self.visited:
            print("A cidade de numero ", self.finalNode, " não foi encontrada")
        else:
            print("O cidade visitada de número ", self.finalNode, " foi encontrada e visitada!")

    def run_dls(self, searchBy, result, maxDepth):
        if searchBy == result:
            return True

        if maxDepth <= 0:
            return False

        for i in self.graph[searchBy]:
            if self.run_dls(i, result, maxDepth - 1):
                return True

        return False

    def dls(self):
        if self.run_dls(self.initialNode, self.finalNode, self.maxDepth):
            print("O cidade visitada de número ", self.finalNode, " foi encontrada e visitada!")

        else:
            print("A cidade de numero ", self.finalNode, " não foi encontrada")

    def bfs(self):
        self.visited = []
        n_visited = [self.initialNode]
        while n_visited:
            node = n_visited.pop(0)
            if node not in self.visited:
                self.visited.append(node)
                neighbourhood = self.graph[node]
                for eachNode in neighbourhood:
                    n_visited.append(eachNode)

    def run_dfs(self, node):
        if node not in self.visited:
            self.visited.append(node)
            for n in self.graph[node]:
                self.run_dfs(n)

    def dfs(self):
        return self.run_dfs(self.initialNode)


start = '1'
goal = '20'
maxDepth = 4

searchInstance = Search(start, goal, maxDepth)

print("Busca em largura - Execução: ")
searchInstance.bfs()
searchInstance.print()

print("\n\n")
searchInstance.clear()

print("Busca em profundidade limitada - Execução: ")
searchInstance.dls()

print("\n\n")
searchInstance.clear()

print("Busca em profundidade  interativa - Execução: ")
searchInstance.dfsInteractive()

print("\n\n")
searchInstance.clear()

print("Busca em profundidade - Execução: ")
searchInstance.dfs()
searchInstance.print()
