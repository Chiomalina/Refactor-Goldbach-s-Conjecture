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
			pairs.append((first, second))

	return pairs


def get_valid_integer() -> int:
	"""
	Keep asking the user for input until a valid integer is provided.
	"""
	while True:
		try:
			return int(input("Enter an even integer greater than 2: "))
		except ValueError:
			print("Error: please enter a valid integer.")


def main() -> None:
	"""
	Main program loop.
	"""
	number = get_valid_integer()

	pairs = goldbach_pairs(number)

	if pairs:
		print(f"\nPrime pairs whose sum is {number}:")
		for p1, p2 in pairs:
			print(f"The number {number} equals the sum of {p1} and {p2}")
	else:
		print(f"No prime pairs found for {number}.")


if __name__ == "__main__":
	main()

