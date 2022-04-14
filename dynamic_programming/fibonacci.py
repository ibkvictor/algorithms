def fibonacci(n):
	table = {
		0:1,
		1:1,
	}
	if n in table:
		return table[n]
	res = fibonacci(n - 1) + fibonacci(n - 2)
	table[n] = res
	return res

print(fibonacci(3))
