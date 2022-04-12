class node:
	#value = None
	#children = []
	def __init__(self, value):
		self.value = value
		self.children = []
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
	def cc_search(self):
		self.mark()
		for node in self.nodes:
			if not self.nodes[node].explored:
				print(self.bfs_ss([node], [])
		
	def mark(self):
		for node in self.nodes:
			self.nodes[node].explored = False
	
	def bfs_ss(self, queue, path):
		queue[0].explored = True
		path.append(queue[0])
		if not queue:
			return path
		if queue[0].children:
			for child in queue[0].children:
				if not child.explored:
					queue.append(child)
		return self.bfs_ss(queue[1:], path)

	def bfs(self, value, queue, path):
		if not queue:
			return None
		path.append(queue[0].value)
		if queue[0].value != value:
			queue += queue[0].children
			return self.dfs(value, queue[1:], path)
		else:
			return [path, queue[0]]

a = [(1,2), (4, 3), (2,4), (6,7), (3,7), (1, 6)]
b = [(1,2), (2,4), (1,3), (3,4), (6,7), (8,10), (8,9), (9,10)]
graphy = Graph(1)
graph_a = Graph(1)
for i, j in b:
	graph_a.add_edge(i,j)
graph_a.cc_search()

for i, j in a:
	graphy.add_edge(i,j)
print(graphy.search(7))
