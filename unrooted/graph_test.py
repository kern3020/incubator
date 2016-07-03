# -*- coding: utf-8 -*-

import unittest

from graph import *

class GraphTest(unittest.TestCase):

    def setUp(self):
        self._g = Graph()
        self._g.insert_edge(1, 2)
        self._g.insert_edge(2, 8)
        self._g.insert_edge(2, 4)
        self._g.insert_edge(4, 5)
        self._g.insert_edge(4, 10)
        self._g.insert_edge(5, 9)
        self._g.insert_edge(6, 10)
        self._g.insert_edge(7, 9)

    def test_1_dump(self):
        self._g.dump()

    def test_2_vist(self):
        #self._g.dfs_visit(2)
        self._g.dfs_visit(4)
