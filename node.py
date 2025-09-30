from dataclasses import dataclass
from state import State
    
@dataclass
class Node:
    state: State
    parent: "Node | None"
    op: str
    g: int
    depth: int

    def path(self):
        node = self
        rev = []
        while node is not None:
            rev.append((node.state, node.g, node.depth, node.op))
            node = node.parent
        return list(reversed(rev))

