def is_prime(number: int) -> bool:
	"""
	Check whether a number is prime.

	A prime number is greater than 1 and divisible only by 1 and itself.
	"""

	if number < 2:
		return False