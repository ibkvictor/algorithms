class node:
        #value = None
        #children = []
        def __init__(self, value):
                self.value = value
                self.children = []

        def add_child(self, node_):
                self.children.append(node_)

class Graph:
        #directed graph
        def __init__(self, value):
                self.edges = []
                self.head = node(value)
                self.nodes = {self.head.value: self.head}

        def add_edge(self, value1, value2):
                if value1 in self.nodes:
                        res = self.search(value1)
                        if not res:
                                node1 = self.nodes[value1]
                        else:
                                _, node1 = res
                        node2 = node(value2)
                        node1.add_child(node2)
                        self.nodes[value2] = node2
                else:
                        node1 = node(value1)
                        node2 = node(value2)
                        self.nodes[value1] = node1
                        self.nodes[value2] = node2
                print(f'{value1} -- {value2}  added')

        def search(self, value):
                #print(value)
                res = bfs(value, self.head, [])
                if not res:
                        print ("value not in graph")
                        return None
                return res

        def bfs(value, curr_node, path):
                path.append(curr_node.value)
                if curr_node.value == value:
                        return [path, curr_node]
                key_node = None
                if curr_node.children:
                        for child in curr_node.children:
                                ret = dfs(value, child, path)
                                if not key_node and ret:
                                        return ret

                else:
                        return None

a = [(1,2), (4, 3), (2,4), (6,7), (3,7), (1, 6)]
graphy = Graph(1)
for i, j in a:
        print(i, j)
        print(graphy.search(3))
        graphy.add_edge(i,j)
print(graphy.search(6))

		
