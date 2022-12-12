import sys
# Setting higher recursion limit
sys.setrecursionlimit(1000000)

data = []
with open("C:\\Repos\\AoC22\\input\\input12.txt", 'r') as f:
    input = f.read()
    data = input.split("\n")

class Node:

    def __init__(self, pos, hight):
        self.pos = pos
        self.hight = hight
        self.neighbors = []
        self.close_positions = []
        self.trace = -1


def create_nodes(d):
    nodes = {}
    start = None
    end = None

    for y, x_row in enumerate(d):
        for x, val in enumerate(x_row):
            pos = (x, y)
            hight = ord(val)-97
            node = Node(pos, hight)
            children = [(x-1, y),(x+1, y),(x, y-1),(x, y+1)]

            for _x, _y in children:
                if _x >= 0 and _x < len(d[0]) and _y >= 0 and _y < len(d):
                    node.close_positions.append((_x, _y))

            if val == "S":
                node.hight = 0
                node.trace = 0
                start = node
            elif val == "E":
                node.hight = 25
                end = node
            nodes[(x, y)] = node
    return (nodes, start, end)

def set_neighbours(node_list):
    for _, node in node_list.items():
        for pos in node.close_positions:
            _node = node_list[pos]
            if _node.hight <= node.hight+1:
                node.neighbors.append(_node)

def walk_node(node):
    for _node in node.neighbors:
        if _node.trace == -1 or _node.trace > node.trace + 1:
            _node.trace = node.trace + 1
            walk_node(_node)


node_list, start, end = create_nodes(data)
set_neighbours(node_list)
walk_node(start)
print(end.trace)
 

node_list, start, end = create_nodes(data)
set_neighbours(node_list)
nodes_with_elevation_zero = [x for _, x in node_list.items() if x.hight == 0]
for node in nodes_with_elevation_zero:
    node.trace = 0

for node in nodes_with_elevation_zero:
    walk_node(node)

print(end.trace)