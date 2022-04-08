import random
def quick_sort(array):
	if len(array) == 1:
		return array
	if len(array) == 2:
		if array[0] > array[1]:
			return [array[1], array[0]]
		return array
	pivot = selection_procedure(array, len(array)//2)
	if not array[pivot] == array[0]:
		array = swap_pivot(pivot, array)
	left, right = arrange_items(array)
	sorted_left = quick_sort(left)
	sorted_right = quick_sort(right)
	return sorted_left + [array[0]] + sorted_right

def arrange_items(array):
	i = 1
	j = len(array)-1
	while i < j:		
		if array[i] > array[0]:
			array = array[:i]+ array[i+1:] + [array[i]]
			j -= 1
		else:
			i+=1
	print((array[1:i],array[i:]))
	return (array[1:i],array[i:])
		
def swap_pivot(i, array):
	return [array[i]] + array[:i] + array[i+1:]

def selection_procedure(array, order):	
	if len(array) == 1:
		return 0
	j = int(random.uniform(0, len(array)))
	print(j, order, array)
	array_part = arrange_items([array[j]] + array[:j] + array[j+1 : ])
	#if len(array_part[0]) == order or len(array_part[0]) + 1 == order:
	if len(array_part[0]) == order:
		return j
	elif len(array_part[0]) > order:
		print("here")
		print(array, array_part, order)
		print(array_part[0], j, array_part[1])
		return selection_procedure(array_part[0], order)
	else:
		print("here instead")
		if(order < 1):
			print(order, array_part, array, "not you")
		return selection_procedure(array_part[1], order - len(array_part[0]))

arrai = [3, 4, 1, 10, 6, 4, 0, 2, 3]
print(quick_sort(arrai))

