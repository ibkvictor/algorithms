def binary_search(array, val):
	left = 0
	right = len(a) - 1
	while left <= right:
		mid = right//2 + left
		if a[mid] > val:
			right = mid - 1
		elif a[mid] < val:
			left = mid + 1
		else: 
			return mid
	return False


a = [2,4,5,6,7,8,8,9,10,12]
v = 4
print(binary_search(a,v))
