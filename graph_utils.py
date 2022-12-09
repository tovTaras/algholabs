from collections import defaultdict


class Graph:

    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def find_mother_util(self, starting_vertex, visited):
        visited.add(starting_vertex)

        for neighbour in self.adjacency_list[starting_vertex]:
            if neighbour not in visited:
                self.find_mother_util(neighbour, visited)

    def dfs_recursive_util(self, starting_vertex, visited, sequence):

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            for neighbour in self.adjacency_list[starting_vertex]:
                self.dfs_recursive_util(neighbour, visited, sequence)
                if neighbour not in sequence: sequence.append(neighbour)
        return sequence

    def dfs(self):
        visited = set()
        sequence = []
        starting_vertex = self.find_mother()
        self.dfs_recursive_util(starting_vertex, visited, sequence)
        sequence.append(starting_vertex)
        return sequence

    def add_edge(self, key, value):
        if isinstance(value, list):
            self.adjacency_list[key] = value
        else:
            self.adjacency_list[key].append(value)

    def find_mother(self):

        visited = set()
        mother_vertex = ''

        for vertex in list(self.adjacency_list):
            if vertex not in visited:
                self.find_mother_util(vertex, visited)
                mother_vertex = vertex

        self.find_mother_util(mother_vertex, visited)
        if len(visited) != len(self.adjacency_list):
            return -1
        else:
            return mother_vertex





def convert_file_to_dict(file_name):
    last_key = []
    d = {}
    with open(file_name) as f:
        for line in f:
            if len(line) > 1:
                (key, val) = line.split()
                if key not in last_key:
                    d[key] = [val]
                    last_key.append(key)
                else:
                    d[key].append(val)

    return d


def write_to_file(file_name, obj_to_write):
    with open(file_name, 'w') as f:
        for element in obj_to_write:
            print(element, end='\n', file=f)


def build_graph(file_name):
    dictionary_to_process = convert_file_to_dict(file_name)
    graph = Graph()
    for key in dictionary_to_process.keys():
        graph.add_edge(key, dictionary_to_process[key])

    return graph
if __name__ == '__main__':

    write_to_file('govern.out', build_graph('govern.in').dfs())




