class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

        self.discovery = 0
        self.finish = 0
        self.color = 'black'

    def add_neighbor(self, v):
        nset = set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    verticies = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.verticies:
            self.verticies[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.verticies and v in self.verticies:
            for key, value in self.verticies.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.verticies.keys())):
            print(key + str(self.verticies[key].neighbors) + "  " + str(self.verticies[key].discovery) + "/" + str(self.verticies[key].finish))
    
    def _dfs(self, vertex):
        global time
        vertex.color = 'red'
        vertex.discovery = time
        time += 1
        for v in vertex.neighbors:
            if self.verticies[v].color == "black":
                self._dfs(self.verticies[v])
        vertex.color = "blue"
        vertex.finish = time
        time += 1
    
    def dfs(self, vertex):
        global time
        time = 1
        self._dfs(vertex)

g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))

for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

for edge in edges: 
    g.add_edge(edge[:1], edge[1:])

g.dfs(a)
g.print_graph()