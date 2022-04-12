def three_sum(array, target):
	res = set()
	if len(array) < 3:
		return res
	array.sort()
	for i in range(len(array) - 2):
		print(i)
		complement = target - array[i]
		print(complement)
		j = 1
		k = len(array) - 1 
		while j < k:
			if array[j] + array[k] > complement:
				k -= 1
			elif array[j] + array[k] == complement:
				res.add((array[i],array[j], array[k]))
				j += 1
				k -= 1
			else:
				j += 1
	return res
nums = [0,0,0]
print(three_sum(nums, 0))
