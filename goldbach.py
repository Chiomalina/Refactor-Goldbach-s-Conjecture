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


def main() -> None:
	"""
	Prompt the user for a number and display its Goldbach prime pairs.
	"""
	while True:
		try:
			number = int(input("Enter an even number greater than 2: "))
			if number <= 2 or number % 2 != 0:
				raise ValueError
			break
		except ValueError:
			print("Invalid input. Please enter an even integer greater than 2.")

	pairs = goldbach_pairs(number)

	if pairs:
		print(f"\nPrime pairs whose sum is {number}:")
		for p1, p2 in pairs:
			print(f"{number} = {p1} + {p2}")
	else:
		print(f"No prime pairs found for {number}.")


if __name__ == "__main__":
	main()

