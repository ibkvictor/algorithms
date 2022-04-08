def count(array):
	value = 0
	if len(array) == 1:
		return 0
	if len(array) == 2:
		return split_count(array[:1], array[1:])
	mid = len(array)//2
	value += count(array[:mid])
	value += count(array[mid:])
	value += split_count(array[:mid], array[mid:])
	return value

def split_count(left, right):
	value = 0
	i = 0
	j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			j+= 1
		else:
			j+=1
			value += 1
		if j == len(right) and i <  len(left) - 1:
			j = 0
			i += 1	
		if j == len(right) and i == len(left) - 1:
			return value
	return value


arrai = [7,6,5,4,3,2,1]
print(count(arrai))
