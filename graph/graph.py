from graph.arch import Arch
from graph.node import Node


class Graph:
    def __init__(self, name):
        self.name = name
        self.nodes = {}
        self.arches = []
        self.rows = 0
        self.cols = 0
        self.start = None
        self.end = None

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = Node(node)

    def add_arch(self, origin, destiny, cost):
        origin = self.nodes[origin]
        destiny = self.nodes[destiny]
        self.arches.append(Arch(origin, destiny, cost))
        origin.add_adjacent(destiny)

    def add_start_end(self, start, end):
        self.start = self.nodes[start]
        self.end = self.nodes[end]

    def bfs(self):
        for node in self.nodes.values():
            node.color = "white"
        self.start.color = "gray"
        queue = [(self.start, [self.start.name])]
        while queue:
            u, path = queue.pop(0)
            if u == self.end:
                return path
            for v in u.ady:
                if v.color == "white":
                    v.color = "gray"
                    queue.append((v, path + [v.name]))
            u.color = "black"
