class Node:
    def __init__(self, id, edges):
        self.id = id
        self.edges = edges
        self.num_edges = len(edges)
        if self.num_edges == 0:
            self.dead_end = True
        else:
            self.dead_end = False
