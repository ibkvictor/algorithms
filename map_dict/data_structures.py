class Node():
	def __init__(self, value):
		self.next = None
		self.value = valuee

class linked_list():
	def __init__(self):
		self.first = None
		self.length = None
		self.last = None

	def insert(self, value):
		if not self.first:
			self.first = Node(value)
			self.last = self.first
		else:
			self.last.next = Node(value)
			self.last = self.last.next

	def search(self, value):
		while True;
			if self.first.value != value:
				
