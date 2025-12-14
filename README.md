# 🧮 Goldbach’s Conjecture – Python Implementation

A clean, refactored Python implementation exploring **Goldbach’s Conjecture**, with a strong focus on **input validation, clean function design, efficiency, and separation of concerns**.

This project was developed as part of a programming assignment and later refactored to reflect **best practices in Python and software engineering**.

---

## 📌 What Is Goldbach’s Conjecture?

**Goldbach’s Conjecture** states:

> Every even integer greater than 2 can be expressed as the sum of two prime numbers.

This project:
- Validates user input
- Finds **all prime pairs** whose sum equals a given even number
- Demonstrates proper use of **functions, loops, exceptions, and return values**

---

## 🎯 Project Goals

- Practice writing **clean, readable Python**
- Apply **exception handling** to prevent crashes
- Separate **logic from presentation**
- Improve algorithm efficiency
- Use **accurate function naming**
- Write code suitable for **testing and reuse**

---

## 🧠 Key Concepts Demonstrated

### ✅ Input Validation
- Handles non-integer input gracefully
- Prevents program crashes using `try / except`
- Repeats input prompt until a valid integer is entered

### ✅ Prime Number Checking
- Efficient prime test using iteration up to `√n`
- Avoids unnecessary computations

### ✅ Goldbach Pair Generation
- Returns a list of prime pairs instead of printing
- Prevents duplicate pairs (e.g. `(3, 7)` and `(7, 3)`)

### ✅ Separation of Concerns
- **Computation functions** return values
- **User interaction and printing** handled in `main()`

---

## 🧩 Project Structure



🧩 Project Structure
```
.
├── goldbach.py
└── README.md

```

---
# 🧪 Example Usage
```
Input: Enter an even integer greater than 2: 
user: 10

Output: The number 10 equals the sum of 3 and 7
        The number 10 equals the sum of 5 and 5
```

---
# 🧪 Example Unit Test
```
def test_goldbach_10():
    assert goldbach_pairs(10) == [(3, 7), (5, 5)]

```

---
# 🧱 Full Implementation

```
def is_prime(n: int) -> bool:
    """
    Check whether a number is prime.
    """
    if n < 2:
        return False

    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False

    return True


def goldbach_pairs(number: int) -> list[tuple[int, int]]:
    """
    Return all pairs of prime numbers whose sum equals `number`.
    """
    pairs = []

    if number <= 2 or number % 2 != 0:
        return pairs

    for first in range(2, number // 2 + 1):
        second = number - first
        if is_prime(first) and is_prime(second):
            pairs.append((first, second))

    return pairs


def main() -> None:
    """
    Program entry point.
    """
    while True:
        try:
            number = int(input("Enter an even integer greater than 2: "))
            if number <= 2 or number % 2 != 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter an even integer greater than 2.")

    pairs = goldbach_pairs(number)

    if pairs:
        for p1, p2 in pairs:
            print(f"The number {number} equals the sum of {p1} and {p2}")
    else:
        print(f"No prime pairs found for {number}.")


if __name__ == "__main__":
    main()

```

# 📚 Lessons Learned
- Why return is preferable to print in logic functions
- How to handle invalid user input safely
- The importance of naming functions accurately
- How small refactors improve testability and readability
- How to think like a junior software engineer, not just a coder

# 👤 Author
Lina Chioma Anaso Software Engineering Student | Full-Stack Developer

📍 Germany

- GitHub: https://github.com/Chiomalina
- LinkedIn: https://linkedin.com/in/lina-chioma-anaso