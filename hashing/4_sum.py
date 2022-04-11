import time
def four_sum(array, target):
	array = sorted(array)
	result = set()
	table = dict()
	for i in range(len(array) - 1):
		for j in range(i+1, len(array)):
			complement = target - array[i] - array[j]
			if complement in table:
				table[complement].add(tuple((i,j)))
			else:
				table[complement] = set()
				table[complement].add(tuple((i,j)))

	for i in range(len(array) - 1):
		for j in range(i+1, len(array)):
			sum = array[i] + array[j]
			if sum in table:
				permit = None
				for pairs in table[sum]:
					if (i not in pairs) and (array[i] not in [array[pairs[0]], array[pairs[1]]]):
						if (j not in pairs) and (array[j] not in [array[pairs[0]], array[pairs[1]]]):
							t = sorted([array[i], array[j],array[pairs[0]], array[pairs[1]]])
							result.add(tuple(t))
	return result

array = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90]
target = 200
start =time.time()
print(four_sum(array, target))
print((time.time() - start) * 1000)
