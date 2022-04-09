def merge():
	pass

def sort(array):
	if len(array) == 1:
		return array
	
	mid = len(array)//2
	
	a = sort(array[:mid])
	b = sort(array[mid:])
	return merge(a, b)

def merge(a, b):
	holder = []
	ptr_a = 0
	ptr_b = 0
	while ptr_a < len(a) and ptr_b < len(b):
		if a[ptr_a] <= b[ptr_b]:
			holder.append(a[ptr_a])
			ptr_a += 1 
		else:
			holder.append(b[ptr_b])
			ptr_b += 1
		if ptr_a == len(a):
			holder += b[ptr_b:]
			break
		if ptr_b == len(b):
			holder += a[ptr_a:]
			break
	return holder

arrai = [2, -2 , 7, 10, 1, 5, 0]

print(sort(arrai))
