class node:
	#value = None
	#children = []
	def __init__(self, value):
		self.value = value
		self.children = []
		self.label = None
		self.explored = False
		self.parents = []
		self.ss_label = None
	
	def add_child(self, node_):
		self.children.append(node_)
	
	def add_parent(self, node_):
		self.parents.append(node_)
	
class Graph:
	#directed graph
	def __init__(self, value):
		self.edges = [] 
		self.head = node(value)
		self.nodes = {self.head.value: self.head}
		
	def add_edge(self, value1, value2):
		if value1 in self.nodes:
			node1 = self.nodes[value1]
			if value2 in self.nodes:
				node2 = self.nodes[value2]
			else:
				node2 = node(value2)
				self.nodes[value2] = node2
			node1.add_child(node2)
			node2.add_parent(node1)

		else:
			node1 = node(value1)
			self.nodes[value1] = node1
			if value2 in self.nodes:
				node2 = self.nodes[value2]
			else:
				node2 = node(value2)
				self.nodes[value2] = node2
			node1.add_child(node2)
			node2.add_parent(node1)
		print(f'{value1} -- {value2}  added')
	
	def search(self, value):
		#print(value)	
		queue = [self.head]
		if self.head.value == value:
			return [queue, self.head]
		queue += self.head.children
		result = self.bfs(value, queue[1:], [self.head.value])
		if not result:
			print ("value not in graph")
			return None
		print(result)
		return result

	def ordering(self):
		self.curr_label = len(self.nodes)
		for node in self.nodes:
			if not self.nodes[node].explored:
				self.dfs(self.nodes[node])

	def scc(self):
		# search for strongly connected components
		self.curr_label = 1
		for node in self.nodes:
			if not self.nodes[node].explored:
				self.dfs_ss(self.nodes[node])
		order = self.mark()
		self.curr_label = 1
		for node in order:
			if not order[node].explored:
				self.dfs_inverse(order[node])
			print(order[node].value, node, order[node].ss_label)
			
	def mark(self):
		# dexploration and marking of finishing time
		order ={i + 1: 0 for i in range(len(self.nodes))}
		for node in self.nodes:
			order[self.nodes[node].ss_label] = self.nodes[node]
			self.nodes[node].explored = False
		return order

	def dfs_ss(self, node):
		# dfs for connected components --first phase
		node.explored = True
		if not node.children:
			node.ss_label = self.curr_label
			self.curr_label += 1
			return
		for child in node.children:
			if not child.explored:
				self.dfs_ss(child)
		node.ss_label = self.curr_label
		self.curr_label += 1
		return

	def dfs_inverse(self, node):
		# dfs inverse for connected components --second phase
		node.explored = True
		if not node.parents:
			node.ss_label = self.curr_label
			self.curr_label += 1
			return
		for parent in node.parents:
			if not parent.explored:
				self.dfs_inverse(parent)
		node.ss_label = self.curr_label
		self.curr_label += 1
		print(f'{node.value}---- node value from dfs')
		return
	
	def dfs(self, node):
		node.explored = True
		if not node.children:
			node.label = self.curr_label
			self.curr_label -= 1
			return
		for child in node.children:
			if not child.explored:
				self.dfs(child)
		node.label = self.curr_label
		self.curr_label -= 1
		return
	
	def bfs(self, value, queue, path):
		if not queue:
			return None
		path.append(queue[0].value)
		if queue[0].value != value:
			queue += queue[0].children
			return self.bfs(value, queue[1:], path)
		else:
			return [path, queue[0]]

a = [(1,2), (3,5), (4,5), (1,3), (1,4), (2,5)]
b = [(1, 7), (4, 1), (7, 4), (3, 9), (6, 3), (9, 6), (7, 9), (6, 8), (8, 2), (5, 8)]
graphy = Graph(1)
graph_a = Graph(1)
for i, j in b:
	graph_a.add_edge(i,j)
graph_a.scc()

#for i, j in a:
#	graphy.add_edge(i,j)
#graphy.ordering()
#for node in graphy.nodes:
#	print(node)
#	print(graphy.nodes[node].label, graphy.nodes[node].value)
#print(graphy.search(7))
