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


def goldback_pairs