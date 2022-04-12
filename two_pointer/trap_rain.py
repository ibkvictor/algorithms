def trap(height):
	area = 0
	i = 0
	j = len(height)-1
	max_i = height[i]
	max_j = height[j]
	while i <= j:
		if max_i <= max_j:
			area += (max([0, max_i - height[i]]))
			print("here", area)
			max_i = max([height[i], max_i])
			i += 1
		else:
			area += (max([0, max_j - height[j]]))
			print("here11", area)
			max_j = max([height[j], max_j])
			j -= 1
	return area		


a = [5,5,1,7,1,1,5,2,7,6]
print(trap(a))
