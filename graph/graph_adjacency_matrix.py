"""Implement graph in an adjacency matrix form


There are two ways to implement graph.
One is 'adjacency matrix' form.

This implementation has some pros and cons.

Pros:
    1. Easy to implement

Cons:
    1. If Edges are sparse, too much spaces are wasted.
       In a matrix form, space takes of V**2. But even if you assume the graph
       is a complete graph, number of edges are (v-1)(v-2) / 2.

Now, I'm gonna make it.

Date : 2018/09/05
"""
class matrix_undirected_weight:
    """Graph in an adjacency matrix form

    Vertex number starts from '1'
    """
    def __init__(self, n):
        self.matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
        self.vector_n = n


    def add_edge(self, src, dest, weight=1):
        self.matrix[src][dest] = weight
        self.matrix[dest][src] = weight


