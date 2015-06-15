import math

"""generate primes"""
def primegenerate(max):
	prime = [1] * max

	for i in range(2, int(math.sqrt(max))):
		if prime[i] == 1:
			for j in range(2 * i, max):
				if j % i == 0:
					prime[j] = 0

	return [i for i in range(2, max) if prime[i] == 1]

"""judge prime"""
def primejudge(number):
	half = number // 2

	for num in range(2, half + 1):
		if(number % num) == 0:
			return False

	return True

""""prime factor"""
def primefactor(number):
	list = []
	i = 0
	primes = prime_generate(number)

	while primes[i] ** 2 <= number:
		if number % primes[i] == 0:
			list.append(primes[i])
			number //= primes[i]
		else:
			i += 1

	list.append(number)
	return list
