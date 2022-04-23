#[ 1 ,2,3]
#return all possible permutuations

#[1,2,3]
#[1,3,2]
#[2,3,1]
#[2,1,3]
#[3,1,2]
#[3,2,1]

#1 - 2 - 3
#  - 3 - 2
#2 - 1 - 3 
#  - 3 - 1
#3 - 1 - 2
#  - 2 - 1

def permutuations(array):
	res = []
	def reccurr(curr):
		if len(curr) == len(array):
			res.append(curr)
			return
		for val in array:
			if val not in curr:
				curr.append(val)
				reccurr(curr)
				curr.pop()		
	reccurr([])
	return res

print(permutuations([3,2,1]))
