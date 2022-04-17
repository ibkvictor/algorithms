class node:
	def __init__(self, value):
		self.value = value
		self.parent = None
		self.left = None
		self.right = None
		self.label = None
		self.visited = None
		
	def add_left(self, left_node):
		self.left = left_node

	def add_right(self, right_node):
		self.right = right_node

class graph:
	def __init__(self, root):
		self.height = 0
		self.root = root
		self.nodes = {root_value: root}

	def in_graph(self, value):
		return (value in self.nodes)

	def add_edge(self, parent_value, child_value):
		if self.in_graph(parent_value:
			if self.in_graph(child_value):
				if child_value < parent_value:
					self.nodes[parent_value].add_left(self.nodes[child_value])
					self.nodes[child_value_value].parent.append(self.nodes[child_value])
				elif child_value > parent_value:
					self.nodes[parent_value].add_right(self.nodes[child_value])
					self.nodes[child_value].parent.append(self.nodes[child_value])

			else:
				child = node(child_value)
				self.nodes[child_value] = child
				if child_value < parent_value:
                                        self.nodes[parent_value].add_left(child)					child.parent.append(self.nodes[parent))
                                elif child_value > parent_value:
                                        self.nodes[parent_value].add_right(child)
                                        child.parent.append(self.nodes[parent_value])

		else:
			parent = node(parent_value)
			self.nodes[parent_value] = parent
			if self.in_graph(child_value):
                                if child_value < parent_value:
                                        self.nodes[parent_value].add_left(self.nodes[child_value])
                                        self.nodes[child_value_value].parent.append(self.nodes[child_value])
                                elif child_value > parent_value:
                                        self.nodes[parent_value].add_right(self.nodes[child_value])                     
                                        self.nodes[child_value].parent.append(self.nodes[child_value])

                        else:
                                child = node(child_value)
                                self.nodes[child_value] = child
                                if child_value < parent_value:
                                        self.nodes[parent_value].add_left(child)                                        child.parent.append(self.nodes[parent))
                                elif child_value > parent_value:
                                        self.nodes[parent_value].add_right(child)
                                        child.parent.append(self.nodes[parent_value]))


	def ancestor(self, value):
		node_ = self.nodes[value]
		res = self.dfs_ancestor(node_.left)
		if res:
			return res
		return None

	def dfs_ancestor(self, node_):
		if not node_:
			return None
		if node_.right:
			res = self.dfs_ancestor(node_.right)
		elif node_.left:
			res = self.dfs_ancestor(node_.left)
		else:
			res = None
		
		if res = None:
			return node_.value
		

	def successor(self, value):
		node_ = self.nodes[value]
                res = self.dfs_successor(node_.right)
                if res:
                        return res
                return None

	def dfs_successor(self, node_):
                if not node_:
                        return None
                if node_.left:
                        res = self.dfs_successor(node_.right)
                elif node_.right:
                        res = self.dfs_successor(node_.left)
                else:
                        res = None
                
                if res = None:
                        return node_.value

	def topological_sort(self, node_):
		self.counter = 0
		for nodes in node_:
			if not node_.visited:
				dfs_topo(node_):
			
		
	def dfs_topo(self, node_):
                if not node_:
                        return None
                if node_.left:
                        self.dfs_successor(node_.right)
                if node_.right:
                        self.dfs_successor(node_.left)
                
		node_.label = self.counter
		self.counter += 1

	def bfs_topo(self, node_):
		if not

node(6)
graphy = graph(6)
a = [(2, 1), (2, 3), (4, 2), (4, 5), (6, 4), (6, 10), (10, 8), (8, 7), (8, 9), (10, 11)]
for i, j in a:
	graphy.add_edge(i, j)
graphy.topological_sort(node_)
graphy.succesor(5)
