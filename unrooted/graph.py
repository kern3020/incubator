# -*- coding: utf-8 -*-

WHITE = 1  # node not visit
GRAY  = 2  # visited but has other nodes
BLACK = 3  # visited and so have other 

class Graph(object):
    def __init__(self):
        self._edges = {}
        self._nodes = {}  # ensure nodes are unique

    def insert_edge(self, index1, index2):
        if index1 not in self._nodes:
            self._nodes[index1] = Node(index1)
        node1 = self._nodes[index1]

        if index2 not in self._nodes:
            self._nodes[index2] = Node(index2)
        node2 = self._nodes[index2]

        # since this is an undirected, record both directory
	# record - node1 -> node2

        if node1.index() not in self._edges:
            self._edges[node1.index()] = [node2]
        else:
            # Is node2 this list?
            exists_p = False
            for node in self._edges[node1.index()]:
                if node.index() == node2.index():
                    exists_p = True
            if not exists_p:
                self._edges[node1.index()].append(node2)

        # ... and node2 -> node1
        if node2.index() not in self._edges:
            self._edges[node2.index()] = [node1]
        else:
            # Is node2 this list?
            exists_p = False
            for node in self._edges[node2.index()]:
                if node.index() == node1.index():
                    exists_p = True
            if not exists_p:
                self._edges[node2.index()].append(node1)


    def dump(self):
        print("dump".format())
        for src in self._edges:
            tmp = "<node: {0}, {1} - ".format(src, len(self._edges[src]))
            first = True
            for dest in self._edges[src]:
                tmp += str(dest)
                tmp += ","
            tmp = tmp[:-1]  # trim trailing comma
            tmp += ">"
            print(tmp)

    def dfs_visit(self, node, depth=0):
        if isinstance( node, int ):
            node = self._nodes[node]
        depth += 1
        if node.color() == WHITE:
            print("\t"*depth + str(node))
            node.set_state(GRAY)
        # import pdb; pdb.set_trace()
        for child in self._edges[node.index()]:
            if child.color() == WHITE:
                self.dfs_visit(child, depth)
        node.set_state(BLACK)
            
class Node (object):
    def __init__(self, value):
        self._state = WHITE
        self._index = value

    def __str__(self):
        state = None
        if self._state == WHITE:
            state = "white"
        elif self._state == GRAY:
            state = "gray"
        else:
            state = "black"
        return "<{0}, {1}>".format(self._index, state)

    def color(self):
        return self._state
    
    def index(self):
        return self._index

    def set_state(self, state):
        self._state = state
