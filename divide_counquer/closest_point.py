def divide(array):
	if len(array) == 1:
		return [65356, None, None]
	elif len(array) == 2:
		return [dist(array[0], array[1]), array[0], array[1]]
	
	value = [65356, None, None]
	mid = len(array)//2

	left_val = divide(array[:mid])
	if left_val[0] < value[0]:
		value = left_val
	right_vale = divide(array[mid:])
	a = right_vale[0]
	if a < value[0]:
		value = right_vale
	conquer_val = conquer(array[:mid], array[mid:])	
	if conquer_val[0] < value[0]:
		value = conquer_val
	return value
	
def conquer(left, right):
	value = [65356, None, None]
	i = 0
	j = 0
	while i < len(left) and j < len(right):
		if dist(left[i], right[j]) < value[0]:
			value = [dist(left[i], right[i]), left[i], right[i]]
			j += 1
		else:
			j += 1
		if j == len(right) and i < len(left) - 1:
			j = 0
			i += 1

		if i >= len(left):
			return value
	return value


def dist(point1, point2):
	return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** (0.5)


arrai = [[0,9], [1,-2], [3, 5], [0,0], [9,1]]
print(divide(arrai))
