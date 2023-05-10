class Node:
    def __init__(self, name):
        self.name = name
        self.color = "white"
        self.ady = []
        self.key = 0

    def add_adjacent(self, ady):
        self.ady.append(ady)
