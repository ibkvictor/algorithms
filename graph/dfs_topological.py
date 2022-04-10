class node:
	#value = None
	#children = []
	def __init__(self, value):
		self.value = value
		self.children = []
		self.label = None
		self.explored = False	
	
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
			node1 = self.nodes[value1]
			if value2 in self.nodes:
				node2 = self.nodes[value2]
			else:
				node2 = node(value2)
				self.nodes[value2] = node2
			node1.add_child(node2)

		else:
			node1 = node(value1)
			self.nodes[value1] = node1
			if value2 in self.nodes:
				node2 = self.nodes[value2]
			else:
				node2 = node(value2)
				self.nodes[value2] = node2
			node1.add_child(node2)
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
graphy = Graph(1)
for i, j in a:
	graphy.add_edge(i,j)
graphy.ordering()
for node in graphy.nodes:
	print(node)
	print(graphy.nodes[node].label, graphy.nodes[node].value)
print(graphy.search(7))
