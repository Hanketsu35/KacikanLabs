# ─────────────────────────────────────────────────────────────────────────────
# CENG113M  |  Lab 9 — Functions II  |  Solutions
# Topics: Recursion · Functions Calling Functions · Modularity
# ─────────────────────────────────────────────────────────────────────────────


# ══════════════════════════════════════════════════════════════════════════════
# PART 1 — Recursion
# ══════════════════════════════════════════════════════════════════════════════

# ── EX 02  Factorial ──────────────────────────────────────────────────────────
def factorial(n):
    # Base case: 0! = 1
    if n == 0:
        return 1
    # Reduction: n! = n * (n-1)!
    return n * factorial(n - 1)

print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(5))  # 120
print(factorial(7))  # 5040


# ── EX 03  Fibonacci ──────────────────────────────────────────────────────────
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(6))   # 8
print(fibonacci(10))  # 55


# ── EX 04  Recursive Power ────────────────────────────────────────────────────
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 0))   # 1
print(power(2, 10))  # 1024
print(power(3, 4))   # 81
print(power(5, 3))   # 125


# ══════════════════════════════════════════════════════════════════════════════
# PART 2 — Functions Calling Functions
# ══════════════════════════════════════════════════════════════════════════════


# ── EX 06  BMI Report ─────────────────────────────────────────────────────────
def calc_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return weight_kg / (height_m * height_m)


def bmi_report(weight_kg, height_cm):
    bmi = calc_bmi(weight_kg, height_cm)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print("BMI:", round(bmi, 1), " -->", category)


bmi_report(70, 175)        # BMI: 22.9  -->  Normal
bmi_report(50, 175)        # BMI: 16.3  -->  Underweight
print(calc_bmi(110, 170))  # 38.1...


# ── EX 07  Grade Report ───────────────────────────────────────────────────────
def average(lst):
    total = sum(lst)
    return total / len(lst)


def grade_report(scores):
    avg = average(scores)

    if avg >= 90:
        letter = "AA"
    elif avg >= 80:
        letter = "BA"
    elif avg >= 70:
        letter = "BB"
    elif avg >= 60:
        letter = "CB"
    else:
        letter = "FF"

    print("Average:", avg, " -->", letter)


grade_report([85, 90, 72, 65])  # Average: 78.0  -->  BB
grade_report([95, 98, 92])      # Average: 95.0  -->  AA
print(average([10, 20, 30]))    # 20.0


# ══════════════════════════════════════════════════════════════════════════════
# PART 3 — Modularity
# ══════════════════════════════════════════════════════════════════════════════

# ── EX 09  Refactor into Modules ──────────────────────────────────────────────
def get_user_info():
    name = input("Name: ")
    age = int(input("Age: "))
    return name, age


def validate_age(age):
    return 0 <= age <= 120


def calculate_birth_year(age):
    return 2026 - age


def display_result(name, year):
    print("Hi", name + "!")
    print("Born in:", year)


def run():
    name, age = get_user_info()
    if not validate_age(age):
        print("Invalid age!")
        return
    year = calculate_birth_year(age)
    display_result(name, year)


# run()  # uncomment to test


# ── EX 10  Shopping Cart ──────────────────────────────────────────────────────
def get_items():
    items = []
    while True:
        name = input("Item name (leave empty to stop): ")
        if name == "":
            break
        price = float(input("Price: "))
        items.append((name, price))
    return items


def apply_discount(price, rate):
    return price * (1 - rate)


def calculate_total(items):
    total = 0
    for item in items:
        total += item[1]
    return total * 1.18


def print_receipt(items, total):
    print("------- RECEIPT -------")
    for item in items:
        print(item[0], "-", item[1], "TL")
    print("-----------------------")
    print("Total (VAT incl.):", round(total, 2), "TL")


def main():
    items = get_items()
    total = calculate_total(items)
    print_receipt(items, total)


# main()  # uncomment to test


# ══════════════════════════════════════════════════════════════════════════════
# BONUS — Number Guessing Game
# ══════════════════════════════════════════════════════════════════════════════

def get_secret():
    return 42   # switch to random.randint(1, 100) when ready


def get_guess():
    return int(input("Your guess: "))


def build_hint(guess, secret):
    if guess > secret:
        direction = "Too high"
    else:
        direction = "Too low"

    if abs(guess - secret) <= 5:
        return direction + " (close!)"
    return direction


def display_final(attempts):
    print("Correct! You got it in", attempts, "attempt(s).")


def game_loop(secret, attempts):
    guess = get_guess()
    if guess == secret:
        display_final(attempts)
        return
    print(build_hint(guess, secret))
    game_loop(secret, attempts + 1)


def play():
    secret = get_secret()
    print("I'm thinking of a number between 1 and 100.")
    game_loop(secret, 1)


# play()  # uncomment to test