import sys

def fourSum(nums, target):
	table = dict()
	res = []
	for i in range(0, len(nums)):
		if nums[i] in table:
			res.append([nums[i], target - nums[i]])
		else:
			table[target - nums[i]] = nums[i]	
	return res
def main():
	#file = sys.stdin
	#n = int(file.readline.strip())
	#for i in range(n):
	#	file.readline().strip()
	nums = [1,0,-1,0,-2,2]
	target = 0
	print(fourSum(nums, target))

main()
