from sqlalchemy import false


def is_prime(number: int) -> bool:
	"""
	Check whether a number is prime.

	A prime number is greater than 1 and divisible only by 1 and itself.
	"""

	if number < 2:
		return False

	# No need to check beyond sqrt(n)
	for divisor in range(2, int(number ** 0.5) + 1):
		if number % divisor == 0:
			return False

	return True


def goldbach_pairs(number: int) -> list[tuple[int, int]]:
	"""
	Return all pairs of prime numbers whose equals 'number'.
	This function is meaningful only for even numbers greater than 2.
	"""
	pairs = []

	if number <= 2 or number % 2 != 0:
		return pairs

	# Only iterate up to number // 2 to avoid duplicate pairs
	for first in range(2, number // 2 + 1):
		second = number - first

		if is_prime(first) and is_prime(second):
			pairs.append(first, second)

	return pairs
