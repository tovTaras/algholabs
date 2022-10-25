import re
from collections import defaultdict


def get_data_from_file():
    file_to_read = open("input.txt")
    lines = file_to_read.readlines()

    with open('input.txt') as f:
        first_line = f.readline()
        start_vertex = first_line

    d = defaultdict(set)
    pattern = r'([0-9]+)(,)([0-9]+)'
    for line in lines:
        x=re.match(pattern, line)
        if(x):
            d[int(x.group(1))].add(int(x.group(3)))
    return int(start_vertex), d


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def find_cycle(self, start):
        start_list = list()
        parent = None
        start_list.append(start)
        start_list.append(parent)
        queue = [start_list]
        visited = set()
        temp_graph = self.graph.copy()

        while len(queue) != 0:
            temp_list = queue.pop()
            temp = temp_list[0]
            if temp not in visited:
                visited.add(temp)
                while len(temp_graph[temp]) != 0:
                    pop = temp_graph[temp].pop()
                    if pop != temp_list[1]:
                        list_to_append = list()
                        list_to_append.append(pop)
                        list_to_append.append(temp)
                        queue.append(list_to_append)
            else:
                print("Cycle found")
                return True
        print("There are no cycle")
        return False


vert, edges = get_data_from_file()
g = Graph(vert)
i = 0
while i < vert:
    s = list(edges[i])
    while len(s) != 0:
        g.add_edge(i, s.pop())
    i = i + 1

print("Start graph ->", g.graph)

f = open("output.txt", "w")
f.write(str(g.find_cycle(3)))
f.close()