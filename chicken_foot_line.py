from typing import List
from domino import Domino

class LineNode:
    def __init__(self, domino: Domino):
        self.domino = domino
        self.next = None

class ChickenFootLine:
    def __init__(self, chicken_foot: LineNode) -> None:
        self.first = chicken_foot

    def add(self, domino: Domino):
        new_node = LineNode(domino)
        new_node.next = self.first
        self.first = new_node

    def get_first_domino(self):
        return self.first.domino