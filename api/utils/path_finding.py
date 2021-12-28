import json

from api.settings import BASE_DIR

PATHS_FILE = BASE_DIR / "data" / "paths.json"

with open(PATHS_FILE, "r") as f:
    PATH_DATA = json.load(f)


class Node:
    def __init__(self, start: int) -> None:
        self.history = [start]

    def new_child(self, val: int) -> "Node":
        node = Node(0)
        node.history = self.history.copy()
        node.history.append(int(val))
        return node

    @property
    def current_position(self) -> int:
        return self.history[-1]

    def __gt__(self, other):
        return len(self)>len(other)

    def __len__(self) -> int:
        return len(self.history)

    def __repr__(self) -> str:
        return ' -> '.join(map(str, self.history))


def find_path(start_location: int, end_location: int) -> list:
    iterations = 0
    pathways = [Node(start_location)]

    while len(pathways):

        iterations += 1
        node = pathways.pop(0)


        for branch in PATH_DATA[str(node.current_position)]:
            
            new_node = node.new_child(branch)
            if int(branch) == end_location:
                return new_node.history

            pathways.append(new_node)
