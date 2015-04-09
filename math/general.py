""""judge parity"""
def Parity_judge(number):
	return (number % 2)

"""gcd"""
def Gcd(number):
	def _gcd_(m, n):
		if n == 0:
			return m
		else:
			return _gcd_(n, m % n)

	m = number[0]
	for i in range(1, len(number)):
		m = _gcd_(m, number[i])

	return m

""""rational number"""
class Rational:
	def __init__(self, n, d):
		self.number = n
		self.denom = d

	def __str__(self):
		return str(self.number) + "/" + str(self.denom)

	def __add__(self, that):
		return Rational(self.number * that.denom + that.number * self.denom, self.denom * that.denom)

	def __sub__(self, that):
		return Rational(self.number * that.denom - that.number * self.denom, self.denom * that.denom)

	def __mul__(self, that):
		return Rational(self.number * that.number, self.denom * that.denom)

	def __truediv__(self, that):
		return Rational(self.number * that.denom, self.denom * that.number)

	def __eq__(self, that):
		return self.number * that.denom == that.number * self.denom
