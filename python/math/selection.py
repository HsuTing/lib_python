"""select algorithm"""
def selection(number):
	def min(m, j):
		if j == len(number):
			return m
		elif number[j] < number[m]:
			return min(j, j + 1)
		else:
			return min(m, j + 1)

	for i in range(0, len(number)):
		m = min(i, i + 1)
		if i != m:
			number[i], number[m] = number[m], number[i]
