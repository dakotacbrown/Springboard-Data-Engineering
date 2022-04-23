class Edge :

    def __init__(self, src, dst, weight) :
         self.src = src 
         self.dst = dst 
         self.weight = weight

class Graph :

    def __init__(self, edge_list, node_cnt) :
         self.edge_list = edge_list
         self.node_cnt  = node_cnt

    def BellmanFord (self, src) :

        # Initialize the distance from the source node S to all other nodes as infinite (999999999) and to itself as 0.
        distance = [999999999999] * self.node_cnt
        distance[src] = 0 

        for node in range(self.node_cnt) :
            for edge in self.edge_list :

                if (distance[edge.dst] > distance[edge.src] + edge.weight) :
                    distance[edge.dst] = distance[edge.src] + edge.weight

        for edge in self.edge_list :

            if (distance[edge.dst] > distance[edge.src] + edge.weight) :
                print("Negative weight cycle exist in the graph")

        for node in range(self.node_cnt) : 
            print("Source Node("+str(src)+") -> Destination Node("+str(node)+") : Length => "+str(distance[node]))

def main() :

    e01 = Edge(0, 1, -1) 
    e05 = Edge(0, 5, 2)
    e12 = Edge(1, 2, 2)
    e15 = Edge(1, 5, -2) 
    e23 = Edge(2, 3, 5)
    e24 = Edge(2, 4, 1)
    e43 = Edge(4, 3, -4) 
    e45 = Edge(4, 5, 3)
    e51 = Edge(5, 1, 2)
    e52 = Edge(5, 2, 3)

    edge_list = [e01, e05, e12, e15, e23, e24, e43, e45, e51, e52]
    node_cnt = 6 
    source_node = 0 
 
    g = Graph(edge_list, node_cnt)
    g.BellmanFord(source_node)

if __name__ == "__main__":
    main()