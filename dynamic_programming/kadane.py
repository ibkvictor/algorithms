#kadane's algorithm

#[-3, -4, 5, -1, 2, -4, 6, -1]
#-3 = -3(max_0)
#-3 -4 = -7 or -4
#-4 + 5 = -1 or 5 (max_1)
#5 + -1 = 4
#4 + 2 = 6 (max_2)
#6 + -4 = 2
#2 + 6 = 8 (max_3)
#8 + -1 = 7

#-3, -4, 5, -1, 2, -4 

import math
def solution(array):
	max_v = -math.inf
	m_sum = 0
	for i in range(len(array)):
		m_sum = max(array[i], array[i] + m_sum)
		max_v = max(m_sum, max_v)
	return max_v


print(solution([-3, -4, 5, -1, 2, -4, 6, -1]))
print(solution([-2, 3, -1, 2]))

