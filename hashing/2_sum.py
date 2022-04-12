def twoSum(nums, target):
	table = {}
	res = set()
	for i in range(len(nums)):
		if nums[i] in table:
			return([i, table[nums[i]]])
			
		else:
			table[target - nums[i]] = i
	return res

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
